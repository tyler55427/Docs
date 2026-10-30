"""训练：加噪样本的噪声预测（MSE）

对应课程 L2_Training.ipynb。x_pert 由闭式公式一次跳到任意 t，
损失为预测噪声与真实噪声的均方误差。
"""

import torch
from torch.utils.data import DataLoader

from config import Config, noise_schedule
from model import ContextUnet


def perturb_input(x, t, noise, ab_t):
    """把图像扰动到第 t 步：sqrt(ab_t) * x + sqrt(1 - ab_t) * noise"""
    return ab_t.sqrt()[t, None, None, None] * x + (1 - ab_t[t, None, None, None]) * noise


def train(cfg: Config, dataloader: DataLoader, use_context: bool = False):
    """训练噪声预测网络并返回模型

    dataloader 产出 (image, label)，label 为上下文向量，use_context=False 时忽略。
    """
    device = cfg.device
    b_t, a_t, ab_t = noise_schedule(cfg, device)

    nn_model = ContextUnet(
        in_channels=3, n_feat=cfg.n_feat, n_cfeat=cfg.n_cfeat, height=cfg.height
    ).to(device)
    optim = torch.optim.Adam(nn_model.parameters(), lr=cfg.lrate)

    for ep in range(cfg.n_epoch):
        nn_model.train()
        # 学习率线性衰减
        optim.param_groups[0]["lr"] = cfg.lrate * (1 - ep / cfg.n_epoch)

        for x, c in dataloader:
            x = x.to(device)
            optim.zero_grad()

            # 随机取时间步并加噪
            noise = torch.randn_like(x)
            t = torch.randint(1, cfg.timesteps + 1, (x.shape[0],)).to(device)
            x_pert = perturb_input(x, t, noise, ab_t)

            # 网络预测噪声，时间步归一化到 [0, 1]
            pred_noise = nn_model(x_pert, t / cfg.timesteps, c=c.to(device) if use_context else None)

            loss = torch.nn.functional.mse_loss(pred_noise, noise)
            loss.backward()
            optim.step()

        # 每个 epoch 存一份权重，形如 model_4.pth
        torch.save(nn_model.state_dict(), f"{cfg.save_dir}/model_{ep}.pth")

    return nn_model
