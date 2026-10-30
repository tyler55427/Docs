"""噪声预测网络

带上下文条件的 U-Net：输入噪声图像与时间步，输出预测的噪声。
时间步与上下文向量分别经 EmbedFC 编码后，拼接到每个尺度上。
"""

import torch
import torch.nn as nn


class ResidualConvBlock(nn.Module):
    """两层 3x3 卷积 + BN + GELU，可选残差连接"""

    def __init__(self, in_channels: int, out_channels: int, is_res: bool = False) -> None:
        super().__init__()
        self.same_channels = in_channels == out_channels
        self.is_res = is_res
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, 3, 1, 1),
            nn.BatchNorm2d(out_channels),
            nn.GELU(),
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(out_channels, out_channels, 3, 1, 1),
            nn.BatchNorm2d(out_channels),
            nn.GELU(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x1 = self.conv1(x)
        x2 = self.conv2(x1)
        if not self.is_res:
            return x2
        # 通道数不同时用 1x1 卷积对齐，再除以 sqrt(2) 归一化方差
        shortcut = x if self.same_channels else nn.Conv2d(x.shape[1], x2.shape[1], 1).to(x.device)(x)
        return (shortcut + x2) / 1.414


class UnetDown(nn.Module):
    """下采样块：两个残差块 + 最大池化"""

    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.model = nn.Sequential(
            ResidualConvBlock(in_channels, out_channels),
            ResidualConvBlock(out_channels, out_channels),
            nn.MaxPool2d(2),
        )

    def forward(self, x):
        return self.model(x)


class UnetUp(nn.Module):
    """上采样块：转置卷积 + 与 skip 拼接 + 两个残差块"""

    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.model = nn.Sequential(
            nn.ConvTranspose2d(in_channels, out_channels, 2, 2),
            ResidualConvBlock(out_channels, out_channels),
            ResidualConvBlock(out_channels, out_channels),
        )

    def forward(self, x, skip):
        return self.model(torch.cat((x, skip), 1))


class EmbedFC(nn.Module):
    """单层前馈网络，把输入维度映射到 emb_dim"""

    def __init__(self, input_dim, emb_dim):
        super().__init__()
        self.input_dim = input_dim
        self.model = nn.Sequential(
            nn.Linear(input_dim, emb_dim),
            nn.GELU(),
            nn.Linear(emb_dim, emb_dim),
        )

    def forward(self, x):
        return self.model(x.view(-1, self.input_dim))


class ContextUnet(nn.Module):
    """噪声预测网络

    编码器逐层下采样，中间层最小；解码器逐层上采样并拼接 skip 连接。
    t 与 context 在每一层都重新嵌入并广播拼接到通道上，使条件作用于所有尺度。
    """

    def __init__(self, in_channels, n_feat=256, n_cfeat=10, height=28):
        super().__init__()
        self.in_channels = in_channels
        self.n_feat = n_feat
        self.n_cfeat = n_cfeat
        self.h = height

        self.init_conv = ResidualConvBlock(in_channels, n_feat, is_res=True)
        self.down1 = UnetDown(n_feat, n_feat)
        self.down2 = UnetDown(n_feat, 2 * n_feat)

        self.to_vec = nn.Sequential(nn.AvgPool2d(4), nn.GELU())

        # 时间步与上下文各一组嵌入，供各尺度使用
        self.timeembed1 = EmbedFC(1, 2 * n_feat)
        self.timeembed2 = EmbedFC(1, 1 * n_feat)
        self.contextembed1 = EmbedFC(n_cfeat, 2 * n_feat)
        self.contextembed2 = EmbedFC(n_cfeat, 1 * n_feat)

        self.up0 = nn.Sequential(nn.ConvTranspose2d(2 * n_feat, 2 * n_feat, self.h // 4, self.h // 4), nn.GroupNorm(8, 2 * n_feat), nn.ReLU())
        self.up1 = UnetUp(4 * n_feat, n_feat)
        self.up2 = UnetUp(2 * n_feat, n_feat)
        self.out = nn.Sequential(
            nn.Conv2d(2 * n_feat, n_feat, 3, 1, 1),
            nn.GroupNorm(8, n_feat),
            nn.ReLU(),
            nn.Conv2d(n_feat, self.in_channels, 3, 1, 1),
        )

    def forward(self, x, t, c=None):
        """x: (B, 3, h, w) 加噪图像，t: (B,1,1,1) 归一化时间步，c: (B, n_cfeat) 上下文"""
        x = self.init_conv(x)
        down1 = self.down1(x)
        down2 = self.down2(down1)
        hiddenvec = self.to_vec(down2)

        # 未给上下文时用零向量，与「无条件训练」一致
        if c is None:
            c = torch.zeros(x.shape[0], self.n_cfeat).to(x)

        temb1, temb2 = self.timeembed1(t), self.timeembed2(t)
        cemb1, cemb2 = self.contextembed1(c), self.contextembed2(c)

        up1 = self.up0(hiddenvec)
        up2 = self.up1(cemb1.view(-1, 2 * self.n_feat, 1, 1) * up1 + temb1.view(-1, 2 * self.n_feat, 1, 1), down2)
        up3 = self.up2(cemb2.view(-1, 1 * self.n_feat, 1, 1) * up2 + temb2.view(-1, 1 * self.n_feat, 1, 1), down1)
        return self.out(torch.cat((up3, x), 1))
