"""推理：DDPM 与 DDIM 两种采样

DDPM —— 每步都用 b_t 注入随机噪声，需 timesteps 次网络调用
DDIM —— 跳过大部分时间步，按固定的步长间隔采样，无随机性，速度快
"""

from dataclasses import dataclass
from typing import List

import torch

from config import Config, noise_schedule
from model import ContextUnet


@dataclass
class Sampler:
    model: ContextUnet
    cfg: Config
    device: torch.device | None = None

    def __post_init__(self):
        self.device = self.device or self.cfg.device
        self.b_t, self.a_t, self.ab_t = noise_schedule(self.cfg, self.device)

    # ---------- 单步去噪 ----------

    def denoise_add_noise(self, x, t, pred_noise, z=None):
        """DDPM 单步：由 x_t 与预测噪声还原 x_{t-1}，并注入方差为 b_t 的噪声

        z=0 时不加噪声，用于最后一步。若始终不加噪声，样本会坍缩。
        """
        if z is None:
            z = torch.randn_like(x)
        noise = self.b_t.sqrt()[t] * z
        mean = (x - pred_noise * ((1 - self.a_t[t]) / (1 - self.ab_t[t]).sqrt())) / self.a_t[t].sqrt()
        return mean + noise

    def denoise_ddim(self, x, t, t_prev, pred_noise):
        """DDIM 单步：确定性跳转，先估 x0 再按 ab_prev 组合"""
        ab = self.ab_t[t]
        ab_prev = self.ab_t[t_prev]
        x0_pred = ab_prev.sqrt() / ab.sqrt() * (x - (1 - ab).sqrt() * pred_noise)
        dir_xt = (1 - ab_prev).sqrt() * pred_noise
        return x0_pred + dir_xt

    # ---------- 完整采样 ----------

    @torch.no_grad()
    def sample_ddpm(self, n_sample: int, context: torch.Tensor | None = None) -> List[torch.Tensor]:
        """DDPM 逐时间步采样，返回各步中间结果用于可视化"""
        x = torch.randn(n_sample, 3, self.cfg.height, self.cfg.height).to(self.device)
        intermediate = []

        for i in range(self.cfg.timesteps, 0, -1):
            t = torch.tensor([i / self.cfg.timesteps])[:, None, None, None].to(self.device)
            # 最后一步不再注入噪声
            z = torch.randn_like(x) if i > 1 else 0
            eps = self.model(x, t, c=context)
            x = self.denoise_add_noise(x, i, eps, z)
            intermediate.append(x.detach().cpu().numpy())

        return intermediate

    @torch.no_grad()
    def sample_ddim(self, n_sample: int, n: int = 20, context: torch.Tensor | None = None) -> List[torch.Tensor]:
        """DDIM 采样：只走 n 步，step_size = timesteps // n"""
        x = torch.randn(n_sample, 3, self.cfg.height, self.cfg.height).to(self.device)
        intermediate = []
        step_size = self.cfg.timesteps // n

        for i in range(self.cfg.timesteps, 0, -step_size):
            t = torch.tensor([i / self.cfg.timesteps])[:, None, None, None].to(self.device)
            eps = self.model(x, t, c=context)
            x = self.denoise_ddim(x, i, i - step_size, eps)
            intermediate.append(x.detach().cpu().numpy())

        return intermediate
