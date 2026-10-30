# VAE

## AE（Autoencoder）

### 目的

压缩图像

### 网络结构

- 编码器：输入图像，输出 1D latent 表示
- 解码器：输入 latent，输出图像

要求latent的维度要低于输入维度

编码器输出固定的latent

### 训练方式

端到端进行训练

#### 损失

根据目标选择一个进行使用

- MSE：适合连续值输入
- L1：对异常值更robust
- BCE：输入归一化到[0,1]或二值图像

## VAE（Variational Autoencoder）

### 目的

- 让编码器的潜空间变成概率空间
- 能够从先验分布中随机采样并**生成**新样本
  - 容易采样的先验：$z \sim p(z)$，$p(z)$通常是标准正态分布 $N(0, I)$
  - 通过解码器生成图像：$x = p_{\theta}(x|z)z$，取分布的均值作为结果

### 困难

- 直接训练数据分布的模型困难，借助边缘似然
  - $p_{\theta}(x) = \int p_{\theta}(x,z)dz  = \int p_{\theta}(x|z)p(z)dz$
  - 积分难以计算，无法直接优化
  - 利用latent分布，假设latent是简单分布，从latent到图像分布也是简单分布
- 已有数据x，想要计算后验分布 $p_{\theta}(z|x)$ 困难，利用编码器近似

### 网络结构

- 编码器：输入图像，输出 latent 维度的 $\mu$ 和 $\sigma$（每个latent维度一个）
- 采样层：采样高斯噪声（**先验分布**），使用重参数化，从 $\mu$ 和 $\sigma$ 采样 latent，即 $z = \mu + \sigma \odot \epsilon$
- 解码器：输入 latent，输出图像分布的 $\mu$ 和 $\sigma$，采样得到图像（取均值/按分布采样）

> **重参数化**：直接采样分布是随机，无法求导用于梯度传播，转化为 $z = \mu + \sigma \odot \epsilon$ 的形式，将随机性交给标准正态，可以求导

### 训练方式

端到端进行训练

#### 损失

同时使用（其实是推导拆分得到的）

- 重建损失：

  - 衡量输入输出图像的差异
  - $L_{recon} = - \mathbb{E}_{q(z|x)}[\log p(x|z)]$
    - 给定所有x生成的z，希望得到x的概率分布最大
    - 高斯假设下，使用MSE
- KL散度损失（正则项）：

  - 衡量的分布差异
  - $L_{KL} = D_{KL}(q(z|x) || p(z))$
    - 希望latent的分布和先验分布（高斯分布：为了生成的时候方便采样）接近

#### 损失推导过程

从训练目标出发，构造可训练的下界，通过优化下界达到优化训练目标的效果

最大化边缘对数似然

$$
\begin{aligned}
\log p_\theta(x)
&=\log \int p_\theta(x,z)\,dz \\[4pt]
&=\log \int q_\phi(z\mid x)\,\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\,dz \\[4pt]
&=\log \mathbb{E}_{q_\phi(z\mid x)}\!\left[\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right] \\[4pt]
&\ge \mathbb{E}_{q_\phi(z\mid x)}\!\left[\log \frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right] \\[4pt]
&=\mathbb{E}_{q_\phi(z\mid x)}\!\left[\log \frac{p_\theta(x\mid z)\,p(z)}{q_\phi(z\mid x)}\right] \\[4pt]
&=\mathbb{E}_{q_\phi(z\mid x)}\!\left[\log p_\theta(x\mid z)+\log p(z)-\log q_\phi(z\mid x)\right] \\[4pt]
&=\mathbb{E}_{q_\phi(z\mid x)}\!\left[\log p_\theta(x\mid z)\right]
-D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\,\|\,p(z)\right) \\[4pt]
&=\mathcal{L}_{\theta,\phi}(x)
\end{aligned}
$$

> **Jensen 不等式**：设 $X$ 是随机变量，若 $f$ 是凸函数，则 $\mathbb{E}[f(X)] \ge f(\mathbb{E}[X])$，若 $f$ 是凹函数，则不等号反向。
> 
> **KL 散度**：设 $P,Q$ 是同一支撑集上的概率分布，则 $D_{\mathrm{KL}}(P\,\|\,Q)=\mathbb{E}_{P}\!\left[\log \frac{p(X)}{q(X)}\right]=\mathbb{E}_{P}\!\left[\log p(X)\right]-\mathbb{E}_{P}\!\left[\log q(X)\right]=\int p(x)\log \frac{p(x)}{q(x)}\,dx$，其中 $p,q$ 为各自的密度，$X\sim P$。
> 性质：
> - 恒有 $D_{\mathrm{KL}}(P\,\|\,Q)\ge 0$，且当且仅当 $P=Q$ 时取零。
> - 不对称：$D_{\mathrm{KL}}(P\,\|\,Q)\neq D_{\mathrm{KL}}(Q\,\|\,P)$。