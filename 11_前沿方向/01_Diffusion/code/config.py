"""扩散模型超参数与噪声调度

将 notebook 里散落的超参数和 b_t / a_t / ab_t 统一到一处，
训练与采样共用同一份调度表。
"""

from dataclasses import dataclass

import torch


@dataclass
class Config:
    # 扩散超参数
    timesteps: int = 500
    beta1: float = 1e-4
    beta2: float = 0.02

    # 网络超参数
    n_feat: int = 64  # 中间特征维度
    n_cfeat: int = 5  # 上下文向量长度
    height: int = 16  # 图像边长，需能被 4 整除

    # 训练超参数
    batch_size: int = 100
    n_epoch: int = 32
    lrate: float = 1e-3

    # 数据与权重
    save_dir: str = "./weights/"

    @property
    def device(self) -> torch.device:
        return torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def noise_schedule(cfg: Config, device=None):
    """线性 beta 调度

    返回 (b_t, a_t, ab_t)，长度均为 timesteps + 1：
        b_t  —— 每一步的噪声方差 beta_t
        a_t  —— 1 - beta_t
        ab_t —— prod(1 - beta_i)，即 alpha 的累乘，缩写 ab_t[t] 对应 alpha_bar_t
    """
    device = device or cfg.device
    b_t = (cfg.beta2 - cfg.beta1) * torch.linspace(0, 1, cfg.timesteps + 1, device=device) + cfg.beta1
    a_t = 1 - b_t
    ab_t = torch.cumsum(a_t.log(), dim=0).exp()
    ab_t[0] = 1
    return b_t, a_t, ab_t
