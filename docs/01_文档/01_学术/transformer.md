##### 为什么自注意力机制在计算时需要对点积结果进行$\sqrt{d_k}$的缩放？
防止维度过大导致方差较大，导致softmax饱和，从而梯度梯度消失

##### Transformer模型中的位置编码如何数学上表示，它解决了什么问题？
位置编码可以使用正弦和余弦函数来表示，公式如下：
$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right)$$
$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right)$$
其中，$pos$表示位置，$i$表示维度索引，$d_{model}$表示模型的维度。

位置编码解决了Transformer模型中缺乏序列位置信息的问题，使得模型能够捕捉输入序列中元素之间的相对和绝对位置关系。

ROPE位置编码的计算方式
ROPE（Rotary Position Embedding）位置编码通过旋转矩阵来实现位置编码。具体计算方式如下：
1. 首先，定义一个旋转矩阵$R(\theta)$，其中$\theta$是一个与位置相关的角度参数。
2. 对于输入序列中的每个位置，计算对应的旋转矩阵$R(\theta_{pos})$，其中$\theta_{pos}$是根据位置计算得到的角度。
3. 将输入的词向量与对应位置的旋转矩阵相乘，得到位置编码后的词向量。
$$PE_{pos} = R(\theta_{pos}) \cdot x_{pos}$$
其中，$x_{pos}$是输入序列中位置为$pos$的词向量。

##### Transformer模型训练中的梯度裁剪是如何数学定义的，它为何重要？
梯度裁剪是一种防止梯度爆炸的技术，其数学定义如下：
$$\text{if } \|g\| > \text{threshold} \text{ then } g = g \cdot \frac{\text{threshold}}{\|g\|}$$

##### 如何数学描述Transformer模型中的学习率预热策略？
学习率预热策略用文字描述：
在训练的初始阶段，学习率从一个较小的值逐渐增加到预设的最大值，然后再逐渐降低。
数学描述：
$$\text{lr}(t) = \begin{cases}
\frac{t}{\text{warmup\_steps}} \cdot \text{max\_lr} & \text{if } t < \text{warmup\_steps} \\
\text{max\_lr} \cdot \left(\frac{t}{\text{warmup\_steps}}\right)^{-0.5} & \text{if } t \geq \text{warmup\_steps}
\end{cases}$$
让初期的模型训练更加稳定

##### Transformer模型中的残差连接如何数学表达，它们解决的问题是什么？
先残差，再层归一化
$$\text{Output} = \text{LayerNorm}(x + \text{Sublayer}(x))$$
残差连接解决了深层网络中的梯度消失问题，使得模型能够更容易地训练更深的网络结构，同时也有助于信息的流动和特征的保留。

##### 为何Transformer 模型中采用 Layer Normalization 而非 Batch Normalization？
Transformer模型中采用Layer Normalization而非Batch Normalization的原因主要有以下几点：
1. **适用于变长序列**：Transformer模型处理的是变长序列，Batch Normalization需要在一个批次内计算均值和方差，而变长序列可能导致批次内的统计量不稳定。Layer Normalization则是针对每个样本进行归一化，不受序列长度的影响。

##### 为什么 Transformer 模型能够有效处理长距离依赖问题？
直接计算序列中任意两个位置之间的关系，而不受距离的限制，使得模型能够捕捉长距离依赖关系。