# Diffusion

## VAE存在的问题

- latent维度不够的时候，细节丢失
- 一步映射，困难

## 假设：

- 一阶马尔可夫链，变换过程的条件分布假设为高斯分布
  - 沿用VAE，条件分布是高斯的，但是多步、**编码器规则固定**、维度相同
- 图像是某个高维分布采样的样本，不是一个确定的结果
- 任何分布加足够的高斯噪声都会变成一个高斯分布

## 建模

- 关键是区分好**分布还是样本**
- 以分布进行理论建模，以样本进行代码编写

### 前向扩散和反向生成过程

#### 理解

- 分布：以当前图像分布作为条件的高斯模型
- 样本：
  - 当前图像的样本点
  - 以当前图像样本的计算结果作为高斯模型的均值和方差
    - 正向是固定的公式计算
    - 逆向是模型预测的噪声和不同采样方法进行计算
  - 采样得到下一步图像的样本点
    - 随机采样高斯噪声，利用均值和方差，得到下一步的图像样本点

### 理论支撑

- 高斯马尔可夫链
- 目标函数
  - 假设训练集中的样本是来自同一个图像分布，利用这些样本计算图像分布的最大化似然
  - 但是分布类型未知，分布参数未知
  - 使用神经网络直接建模真实图像的分布类型，使用训练集样本估计分布参数
  - 但是建模是每一步，最大化似然是每一步的积分，不可计算，改用神经网络建模逆向的高斯过程
- 通过变分推断，将最大化（不可直接计算的对数似然）转化为最大化其可计算的下界——证据下界 (ELBO)
- 离散的极限是SDE

## 前向扩散和反向生成的公式

- 前向扩散
  - 定义为马尔可夫链：$q(x_{1:T} | x_0) = \prod_{t=1}^{T} q(x_t | x_{t-1})$
  - 每一步加噪的定义：$q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-\beta_t} x_{t-1}, \beta_t I)$
    - $\beta_t$ 是第 $t$ 步的噪声强度
    - $\sqrt{1-\beta_t}$ 是保留一部分上一时刻的图像信息
    - 使用平方根的原因是为了在每一步加噪的时候保持方差的一致性
  - 变量替换重写定义：$q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{\alpha_t} x_{t-1}, (1-\alpha_t) I)$
    - $\alpha_t = 1-\beta_t$
    - 为了简化公式
  - 推导到任意程度的噪声：$q(x_t | x_0) = \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0, (1-\bar{\alpha}_t) I)$
    - $\bar{\alpha}_t = \prod_{s=1}^{t} \alpha_s$
  - 从分布到采样：$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon_t, \quad \epsilon_t \sim \mathcal{N}(0, I)$
    - 当 $t$ 很大时，$\bar{\alpha}_t$ 趋近于 0，$x_t$ 趋近于纯噪声，所以生成的时候可以从纯噪声开始
- 反向生成
  - 模型联合分布：$p_\theta(x_{0:T}) = p(x_T) \prod_{t=1}^{T} p_\theta(x_{t-1} | x_t)$
  - 每一步的条件分布：$p_\theta(x_{t-1} | x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \sigma_\theta^2(x_t, t) I)$
    - 模型预测均值和方差，用于生成下一步的图像样本点
      - 实际上diffusion不预测方差，固定方差为常量

## 训练目标

最大化真实图像分布的似然

#### 损失推导过程

从训练目标出发，构造可训练的下界，通过优化下界达到优化训练目标的效果

$$
\begin{aligned}
\log p_\theta(x_0)
&=\log \int p_\theta(x_{0:T})\,dx_{1:T} \\[4pt]
&=\log \int q(x_{1:T}\mid x_0)\,\frac{p_\theta(x_{0:T})}{q(x_{1:T}\mid x_0)}\,dx_{1:T} \\[4pt]
&=\log \mathbb{E}_{q(x_{1:T}\mid x_0)}\!\left[\frac{p_\theta(x_{0:T})}{q(x_{1:T}\mid x_0)}\right] \\[4pt]
&\ge \mathbb{E}_{q(x_{1:T}\mid x_0)}\!\left[\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}\mid x_0)}\right] \\[4pt]
&=\mathbb{E}_{q}\!\left[\log \frac{p(x_T)\prod_{t=1}^{T} p_\theta(x_{t-1}\mid x_t)}{\prod_{t=1}^{T} q(x_t\mid x_{t-1})}\right] \\[4pt]
&=\mathbb{E}_{q}\!\left[\log p(x_T)+\sum_{t=1}^{T}\log p_\theta(x_{t-1}\mid x_t)-\sum_{t=1}^{T}\log q(x_t\mid x_{t-1})\right] \\[4pt]
&=\mathcal{L}_{\theta,\phi}(x_0)
\end{aligned}
$$

$$
\mathcal{L}_{\theta,\phi}(x_0)
=\underbrace{\mathbb{E}_{q}\!\left[\log p_\theta(x_0\mid x_1)\right]}_{L_0}
-\underbrace{D_{\mathrm{KL}}\!\left(q(x_T\mid x_0)\,\|\,p(x_T)\right)}_{L_T}
-\underbrace{\sum_{t=2}^{T}\mathbb{E}_{q}\!\left[D_{\mathrm{KL}}\!\left(q(x_{t-1}\mid x_t,x_0)\,\|\,p_\theta(x_{t-1}\mid x_t)\right)\right]}_{L_{t-1}}
$$

- 第一项：重建损失
- 第二项：KL散度损失，衡量前向扩散分布与先验分布的差异，通常接近常数，训练时忽略
- 第三项：KL散度损失，衡量反向生成分布与真实后验的差异，是训练的主要部分

### 推导损失第三项的真实后验

真实后验根据贝叶斯公式：

$$
q(x_{t-1} | x_t, x_0) = \frac{q(x_t | x_{t-1}, x_0) q(x_{t-1} | x_0)}{q(x_t | x_0)}
$$

由于前向扩散的马尔可夫性质，$q(x_t | x_{t-1}, x_0) = q(x_t | x_{t-1})$，因此真实后验可以进一步简化，且由于右边三项都是高斯分布，所以真实后验分布也是高斯分布

$$
\begin{aligned}
q(x_{t-1} | x_t, x_0)
&\propto q(x_t | x_{t-1}) q(x_{t-1} | x_0) \\[4pt]
&\propto \exp\left(-\frac{\left\|x_t - \sqrt{\alpha_t} x_{t-1}\right\|^2}{2\beta_t} - \frac{\left\|x_{t-1} - \sqrt{\bar{\alpha}_{t-1}} x_0\right\|^2}{2(1-\bar{\alpha}_{t-1})}\right) \\[4pt]
&\propto \exp\left(-\frac{1}{2\tilde{\beta}_t}\left\|x_{t-1} - \tilde{\mu}_t\right\|^2\right)
\end{aligned}
$$

$$
\tilde{\mu}_t(x_t, x_0) = \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t} x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t} x_0, \qquad
\tilde{\beta}_t = \frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t
$$

真实后验的均值是 $x_0$ 和 $x_t$ 的线性组合，为反向生成的最合理的中心位置，训练的时候模型应该学会预测这个均值

### 预测噪声而不是均值

- 想要得到真实后验的均值，需要知道原图（可以模型直接预测，但是作者选择按下面方式进行转换）
- 根据确定的前向公式，能够求解得到原图，即由 $x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t}\,\epsilon$ 得到 $x_0 = \frac{x_t - \sqrt{1-\bar{\alpha}_t}\,\epsilon}{\sqrt{\bar{\alpha}_t}}$
- 将预测原图转换为预测噪声：把上式代回真实后验的均值

$$
\begin{aligned}
\tilde{\mu}_t
&= \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t} x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t} \cdot \frac{x_t - \sqrt{1-\bar{\alpha}_t}\,\epsilon}{\sqrt{\bar{\alpha}_t}} \\[4pt]
&= \left(\frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t} + \frac{\beta_t}{\sqrt{\alpha_t}(1-\bar{\alpha}_t)}\right) x_t - \frac{\beta_t}{\sqrt{\alpha_t}\sqrt{1-\bar{\alpha}_t}}\,\epsilon \\[4pt]
&= \frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1}) + \beta_t/\sqrt{\alpha_t}}{1-\bar{\alpha}_t} x_t - \frac{\beta_t}{\sqrt{\alpha_t}\sqrt{1-\bar{\alpha}_t}}\,\epsilon \\[4pt]
&= \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon\right)
\end{aligned}
$$

$$
\mu_\theta(x_t,t) = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon_\theta(x_t,t)\right)
$$

### 最终损失

- 模型均值与真实后验均值的差异
- 代入KL散度公式中
- 最后忽略权重，就是MSE

## 推理DDPM均值采样

$$
x_{t-1} = \mu_\theta(x_t, t) + \sigma_t z = \frac{1}{\sqrt{\alpha_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\,\epsilon_\theta(x_t, t)\right) + \sigma_t z, \qquad z \sim \mathcal{N}(0, I)
$$

## 问题

- 为什么加噪是直接从0到t，模型预测的噪声也是从0到t，但是实际推理的时候却是从t到t-1，而不是从t到0？
  - 根据损失的第三项KL项，本质上是学习的从t到t-1的均值预测，只是能够通过噪声得到均值
