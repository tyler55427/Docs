# 五、贝叶斯推理方法：MCMC 近似
## 为什么需要 MCMC

- **网格近似**：计算量大，不适合高维
- **准确数学分析**：不一定能找到共轭先验
- **MCMC**：从后验 $p(\theta|D)$ 采样很多，近似 $p(\theta|D)$

> MCMC 优势：先验 $p(\theta)$ 任意；不用算 $p(D)$（不用归一化）

## 蒙特卡洛方法

用大量离散样本近似目标概率分布。

## 马尔科夫链

下一步状态只依赖于当前状态。

## Metropolis 算法

类比：岛屿游玩时间与面积成正比。

**算法**：

1. 当前采样 $\theta_{\text{current}}$
2. 提议分布：$\theta_{\text{current}} \rightarrow \theta_{\text{proposed}}$（对称提议如 $\frac{1}{2}$ 到左右）
3. 接受建议：$p_{\text{move}} = \min\left(\frac{P(\theta_{\text{proposed}})}{P(\theta_{\text{current}})}, 1\right)$
4. 生成均匀随机数 $\epsilon \in [0,1]$：若 $\epsilon < p_{\text{move}}$ 则接受 $\theta_{\text{proposed}}$，否则留在 $\theta_{\text{current}}$

**收敛证明**：$\frac{P(\theta_t \to \theta_{t+1})}{P(\theta_{t+1} \to \theta_t)} = \frac{P(\theta_{t+1})}{P(\theta_t)}$

## 提议分布

| 类型 | 说明 |
|------|------|
| ① 独立采样 | $q(\theta^*\|\theta) = q(\theta^*)$，要求 $q$ 与目标分布 $p$ 接近 |
| ② 随机游走 | $q(\theta^*\|\theta) = N(\theta^*\|\theta, \sigma^2)$，以当前位置为中心的正态分布 |

**Random Walk Metropolis (RWM)**：
$$\theta^* = \theta + \epsilon, \quad \epsilon \sim N(0,1)$$

接受率与步长 $\sigma$ 权衡：$\sigma$ 小则慢，$\sigma$ 大则接受率低。**目标接受率约 50%**。

## 有效样本数量 (ESS)

ESS 衡量采样样本的聚集度：
$$\text{ESS} = \frac{N}{1 + 2\sum_{k=1}^K \text{ACF}(k)}$$

- 自相关性（ACF）：滞后步数 $k$ 的相关性
- 聚集度高 → 有效样本少

## Gibbs 采样

特殊的 Metropolis-Hastings 算法，改善接受率，更快收敛。

**与 Metropolis 的区别**：
- 多维参数，每步只改变一个参数
- 通过 $p(\theta_i | \vec{\theta}_{-i}, D)$ 采样

**提议分布**：$q(\theta^*|\vec{\theta}) = p(\theta_i^*|\vec{\theta}_{-i}, D)$

**接受率**：由于提议分布为条件分布，接受率恒为 1。

**优势**：
- 后验 $p(\theta|D)$ 难算，但条件分布 $p(\theta_i|\theta_{-i}, D)$ 容易采样

**局限**：
- 条件分布难计算时不易采样
- 高相关性参数会导致采样慢

### 预热阶段 (Burn-in)

从不同初始值开始，轨迹在初始值附近差异大。开始的无效样本应丢弃（未收敛到正确后验）。

## 多维分布的采样

对于多硬币问题（独立参数 $\theta_1, \theta_2$）：

$$p(D|\theta_1, \theta_2) = \prod_{y_{1j}\in D_1} p(y_{1j}|\theta_1) \prod_{y_{2j}\in D_2} p(y_{2j}|\theta_2)$$

Metropolis：使用二维提议分布；Gibbs：逐个参数采样，可得边缘分布。

## 小结：三种推理方法对比

| 方法 | 适用场景 | 特点 |
|------|----------|------|
| 网格近似 | 低维、精确 | 计算量大 |
| 准确数学分析 | 可找到共轭先验 | 精确解，表达能力有限 |
| MCMC | 任意先验、高维 | 近似解，需收敛诊断 |
| 变分近似 | 大数据 | 近似为优化问题 |

> 变分推断适合大数据（PyMC 在大数据上慢）
