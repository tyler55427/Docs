# PyTorch 深度学习

基于 PyTorch + d2l（动手学深度学习）的深度学习学习笔记，涵盖从张量操作、线性回归到 CNN/RNN 的核心知识链。

**目录**
1. [张量操作与自动求导](#1-张量操作与自动求导)
2. [线性回归](#2-线性回归)
3. [Softmax 回归与图像分类](#3-softmax-回归与图像分类)
4. [MLP 与模型构建](#4-mlp-与模型构建)
5. [卷积神经网络](#5-卷积神经网络)
6. [循环神经网络与时间序列](#6-循环神经网络与时间序列)
7. [概率基础](#7-概率基础)
8. [草稿与实验](#8-草稿与实验)

## 1 张量操作与自动求导

来源：`A1.py` — 张量的创建、运算、广播、范数，以及自动求梯度、分离计算 `detach()`。

```python
import torch

x = torch.arange(12)
print(x)
print(x.shape)
print(x.numel())
x = x.reshape(3, 4)
# 自动计算
# x.reshape(-1, 3)

torch.zeros((2, 3, 4))
torch.ones((2, 3, 4))

# 正态分布
torch.randn(3, 4)

# 张量连结
y = torch.arange(12).reshape(3, 4)
print(torch.cat((x, y), dim=0))  # dim 是张量轴
print(torch.cat((x, y), dim=1))

print(x == y)

print(x.sum())
```

### 1.1 广播机制与索引

```python
print('广播机制')
a = torch.arange(3).reshape(3, 1)
b = torch.arange(2).reshape(1, 2)
print(a + b)

print(x[-1])
# 左开右闭
print(x[1:3])
x[1, 2] = 9
```

### 1.2 降维求和与线性代数运算

- `sum(axis)` 沿指定轴求和
- `keepdim=True` 保持维度
- `cumsum` 累积求和
- 点积 `dot`、向量积 `mv`、矩阵乘法 `mm`、范数 `norm`

```python
# 降维
x = torch.arange(12)
x = x.reshape((3, 4))
print(x.sum([0]))  # 将每列的元素求和
print(x.sum(axis=1))  # 将每行的元素求和

# 非降维求和
print(x.sum(axis=1, keepdim=True))
print(x.cumsum(axis=0))

# 点积
x = torch.arange(4)
y = torch.arange(4)
print(torch.dot(x, y))
print(torch.sum(x * y))

# 向量积
x = torch.arange(40).reshape(8, 5)
y = torch.arange(5)
print(torch.mv(x, y))

# 矩阵乘法
x = torch.arange(20, dtype=torch.float32).reshape(4, 5)
y = torch.ones(40).reshape(5, 8)
print(torch.mm(x, y))

# 范数
u = torch.tensor([-3.0, 4.0])
print(torch.norm(u))  # 二维范数
print(torch.abs(u).sum())  # 一维范数
```

### 1.3 自动求梯度

梯度与 `x` 有相同的形状。如果函数是直接由向量 `x` 构成的，可以直接求导得到梯度。

- `requires_grad_(True)` 开启梯度追踪
- `backward()` 反向传播自动计算梯度
- `x.grad` 储存梯度
- **默认 PyTorch 的梯度会累积**，需用 `x.grad.zero_()` 清除

```python
x = torch.arange(4.0)
x.requires_grad_(True)
y = 2 * torch.dot(x, x)
y.backward()  # 反向传播函数，自动计算梯度
print(x.grad)  # 储存梯度
print(x.grad == 4 * x)

# 默认 pytorch 的梯度会累积，要清除
x.grad.zero_()
y = x.sum()
y.backward()
print(x.grad)

# 对于 y 不是标量的梯度是一个高阶张量
x.grad.zero_()
y = x * x
y.sum().backward()  # 这里没有计算微分矩阵，只是计算偏导数之和
print(x.grad)
```

### 1.4 分离计算 detach

将 `y` 作为常数分离出来，不参与 `x` 的反向微分计算。

控制流求梯度的例子：当函数包含条件分支时，梯度仍然可以正确计算。

```python
# 分离计算
x.grad.zero_()
y = x * x
u = y.detach()
z = u * x
z.sum().backward()
print(x.grad)

# 控制流求梯度
a = torch.randn(size=(), requires_grad=True)

def f(a):
    b = 2 * a
    while b.norm() < 1000:
        b = b * 2
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b
    return c

d = f(a)
d.backward()
print(a.grad == d / a)
```

## 2 线性回归

来源：`A2.py`、`Linear.py`、`A3-2-1.py` — 从零实现到简洁实现。

线性回归模型：$\hat{y} = Xw + b$，损失函数为均方误差 $\ell = \frac{1}{2}(\hat{y} - y)^2$。

### 2.1 从零实现

包括：正态分布可视化、合成数据集、小批量数据迭代器、线性回归模型、均方损失、小批量 SGD。

```python
import math
import numpy as np
import torch
import random
from d2l import torch as d2l

# 正态分布
def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma ** 2)
    return p * np.exp(-0.5 / sigma ** 2 * (x - mu) ** 2)

w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# 生成数据集
def synthetic_data(w, b, num_examples):
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

# 打乱并小批量获取数据集的样本
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i:min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]

def linreg(X, w, b):
    # 线性回归模型
    return torch.matmul(X, w) + b

def squared_loss(y_hat, y):
    # 均方损失
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

def sgd(params, lr, batch_size):
    # 小批量随机梯度下降
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()
```

```python
# 开始训练
batch_size = 10
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)
        l.sum().backward()
        sgd([w, b], lr, batch_size)
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')
```

### 2.2 简洁实现

使用 `nn.Linear`、`MSELoss`、`TensorDataset`/`DataLoader`、`optim.SGD` 的 API 实现。

```python
import numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = d2l.synthetic_data(true_w, true_b, 1000)

def load_array(data_arrays, batch_size, is_train=True):
    """构造一个 PyTorch 数据迭代器"""
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

batch_size = 10
data_iter = load_array((features, labels), batch_size)

# nn 是神经网络的缩写
from torch import nn

# 第一层的输入参数个数，和输出参数个数
net = nn.Sequential(nn.Linear(2, 1))

# 设置第一层的权重和偏置
net[0].weight.data.normal_(0, 0.01)
net[0].bias.data.fill_(0)

# 调用平方范数的损失函数
loss = nn.MSELoss()

# 指定优化算法为小批量随机梯度下降
trainer = torch.optim.SGD(net.parameters(), lr=0.03)

num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X), y)
        trainer.zero_grad()
        l.backward()
        trainer.step()
    l = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l:f}')

w = net[0].weight.data
print('w 的估计误差：', true_w - w.reshape(true_w.shape))
b = net[0].bias.data
print('b 的估计误差：', true_b - b)
```

### 2.3 自实现版本（A3-2-1）

与 2.1 类似但数据参数不同，使用更大的权重值。

```python
import torch
from d2l import torch as d2l
import random

true_w = torch.tensor([2345, -3344.4])
true_b = 234.435

X = torch.normal(0, 1, (1000, 2))
Y = torch.matmul(X, true_w) + true_b
Y += torch.normal(0, 0.01, Y.shape)

w = torch.normal(0, 0.01, (2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

batch_size = 10
lr = 0.03
num_epochs = 5

def net(X):
    return torch.matmul(X, w) + b

def loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()

def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = indices[i:min(i + batch_size, num_examples)]
        yield features[batch_indices], labels[batch_indices]

for epoch in range(num_epochs):
    for X_batch, Y_batch in data_iter(batch_size, X, Y):
        l = loss(net(X_batch), Y_batch)
        l.sum().backward()
        sgd([w, b], lr, batch_size)
    with torch.no_grad():
        train_l = loss(net(X), Y)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')
        print(f'w: {w}, b: {b}')
```

## 3 Softmax 回归与图像分类

来源：`A3-3-1.py`、`A3-2-2.py` — Fashion-MNIST 数据集加载与 softmax 回归从零实现。

Softmax 回归用于多类分类：$\hat{y}_j = \frac{\exp(o_j)}{\sum_k \exp(o_k)}$，损失函数为交叉熵。

### 3.1 Fashion-MNIST 数据集加载

- `ToTensor` 将图像从 PIL 类型变换成 32 位浮点数格式，并除以 255 使像素值在 0~1 之间
- `Compose` 组合多个变换
- `DataLoader` 加载数据，支持多进程读取

```python
import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l

def get_dataloader_workers():
    """使用 4 个进程来读取数据"""
    return 4

def load_data_fashion_mnist(batch_size, resize=None):
    """下载 Fashion-MNIST 数据集，然后将其加载到内存中"""
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(
        root="../data", train=True, transform=trans, download=True)
    mnist_test = torchvision.datasets.FashionMNIST(
        root="../data", train=False, transform=trans, download=True)
    return (data.DataLoader(mnist_train, batch_size, shuffle=True,
                            num_workers=get_dataloader_workers()),
            data.DataLoader(mnist_test, batch_size, shuffle=False,
                            num_workers=get_dataloader_workers()))

train_iter, test_iter = load_data_fashion_mnist(32, resize=64)
for X, y in train_iter:
    print(X.shape, X.dtype, y.shape, y.dtype)
    break
```

### 3.2 Softmax 回归从零实现

包括：`softmax`、`cross_entropy`、`accuracy`、`Accumulator` 累加器、`Animator` 动态绘图、训练循环 `train_ch3`、预测可视化。

```python
import torch
from IPython import display
from d2l import torch as d2l

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

num_inputs = 784
num_outputs = 10

W = torch.normal(0, 0.01, size=(num_inputs, num_outputs), requires_grad=True)
b = torch.zeros(num_outputs, requires_grad=True)

X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
X.sum(0, keepdim=True), X.sum(1, keepdim=True)

def softmax(X):
    X_exp = torch.exp(X)
    partition = X_exp.sum(1, keepdim=True)
    return X_exp / partition  # 这里应用了广播机制

X = torch.normal(0, 1, (2, 5))
X_prob = softmax(X)
X_prob, X_prob.sum(1)

def net(X):
    return softmax(torch.matmul(X.reshape((-1, W.shape[0])), W) + b)

y = torch.tensor([0, 2])
y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
y_hat[[0, 1], y]

def cross_entropy(y_hat, y):
    return - torch.log(y_hat[range(len(y_hat)), y])

cross_entropy(y_hat, y)
```

```python
def accuracy(y_hat, y):
    """计算预测正确的数量"""
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())

def evaluate_accuracy(net, data_iter):
    """计算在指定数据集上模型的精度"""
    if isinstance(net, torch.nn.Module):
        net.eval()  # 将模型设置为评估模式
    metric = Accumulator(2)  # 正确预测数、预测总数
    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]

class Accumulator:
    """在 n 个变量上累加"""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
```

```python
def train_epoch_ch3(net, train_iter, loss, updater):
    """训练模型一个迭代周期（定义见第 3 章）"""
    # 将模型设置为训练模式
    if isinstance(net, torch.nn.Module):
        net.train()
    # 训练损失总和、训练准确度总和、样本数
    metric = Accumulator(3)
    for X, y in train_iter:
        # 计算梯度并更新参数
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            # 使用 PyTorch 内置的优化器和损失函数
            updater.zero_grad()
            l.mean().backward()
            updater.step()
        else:
            # 使用定制的优化器和损失函数
            l.sum().backward()
            updater(X.shape[0])
        metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
    # 返回训练损失和训练精度
    return metric[0] / metric[2], metric[1] / metric[2]

class Animator:
    """在动画中绘制数据"""
    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1,
                 figsize=(3.5, 2.5)):
        # 增量地绘制多条线
        if legend is None:
            legend = []
        d2l.use_svg_display()
        self.fig, self.axes = d2l.plt.subplots(nrows, ncols, figsize=figsize)
        if nrows * ncols == 1:
            self.axes = [self.axes, ]
        # 使用 lambda 函数捕获参数
        self.config_axes = lambda: d2l.set_axes(
            self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        self.X, self.Y, self.fmts = None, None, fmts

    def add(self, x, y):
        # 向图表中添加多个数据点
        if not hasattr(y, "__len__"):
            y = [y]
        n = len(y)
        if not hasattr(x, "__len__"):
            x = [x] * n
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].cla()
        for x, y, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x, y, fmt)
        self.config_axes()
        display.display(self.fig)
        display.clear_output(wait=True)

def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):
    """训练模型（定义见第 3 章）"""
    animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                        legend=['train loss', 'train acc', 'test acc'])
    for epoch in range(num_epochs):
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        animator.add(epoch + 1, train_metrics + (test_acc,))
    train_loss, train_acc = train_metrics
    assert train_loss < 0.5, train_loss
    assert train_acc <= 1 and train_acc > 0.7, train_acc
    assert test_acc <= 1 and test_acc > 0.7, test_acc
```

```python
lr = 0.1

def updater(batch_size):
    return d2l.sgd([W, b], lr, batch_size)

num_epochs = 10
train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs, updater)

def predict_ch3(net, test_iter, n=6):
    """预测标签（定义见第 3 章）"""
    for X, y in test_iter:
        break
    trues = d2l.get_fashion_mnist_labels(y)
    preds = d2l.get_fashion_mnist_labels(net(X).argmax(axis=1))
    titles = [true + '\n' + pred for true, pred in zip(trues, preds)]
    d2l.show_images(
        X[0:n].reshape((n, 28, 28)), 1, n, titles=titles[0:n])

predict_ch3(net, test_iter)
d2l.plt.show()
```

## 4 MLP 与模型构建

来源：`A3-3-2.py` — 多层感知机、自定义模块、参数管理、初始化、Dropout、模型保存/加载，并包含卷积和 BatchNorm 的片段。

### 4.1 张量操作补充与索引

Python 列表与 tensor 索引的差异，内存重新分配问题。

```python
import torch
from d2l import torch as d2l
import random

X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
X[1, 2] = 9
print(X)
# 和 python 不同的取值方式
a = [[1, 2, 3], [4, 5, 6]]
a[1][2] = 9
print(a)

# 内存是否重新分配
Y = X.clone()
print(id(Y))
Y = Y + X
print(id(Y))

Y[:] = X + Y
print(id(Y))

# 线性代数
X = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
Y = torch.tensor([[10.0, 20.0], [30.0, 40.0]])
print(X.mean(), X.sum() / X.numel())
```

### 4.2 自动微分与分离计算

```python
# 自动微分（只能计算在某一个值的导数）
X = torch.arange(4.0, requires_grad=True)
Y = X * X
# 只有输出是 scalar（标量），才能无参数调用，否则要传入一个 gradient 参数，
# 指定微分函数关于 self 的梯度
# 等价于 Y.backward(torch.ones(len(X)))
Y.sum().backward()
print(X.grad)

# 分离计算
X.grad.zero_()
Y = X * X
# 将 Y 作为常数分离出来，不参与 X 的反向微分计算
U = Y.detach()
Z = U * X
Z.sum().backward()
print(X.grad)
# 二阶导数应该怎么求？
```

### 4.3 小批量抽样与权重衰减/暂退法

```python
# 小批量抽样
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = indices[i:min(i + batch_size, num_examples)]
        yield features[batch_indices], labels[batch_indices]

f = torch.tensor([2, 3, 4, 5])
l = torch.tensor([1, 2, 3, 4])
# 传入的是 tensor，不是 list
# tensor 可以通过列表索引来生成新的 tensor
for x, y in data_iter(2, f, l):
    print(x, y)
```

```python
# 小批量随机梯度下降（概念实现）
def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            # 每个参数都有一个梯度，它们是不同的
            # 关于不同参数的有不同的偏导，它们的梯度是分开计算的
            param -= lr * param.grad / batch_size
            param.grad.zero_()

net = torch.nn.Sequential(torch.nn.Linear(2, 1))
net[0].weight.data.normal_(0, 0.01)
net[0].bias.data.fill_(0)
loss = torch.nn.MSELoss()
trainer = torch.optim.SGD(net.parameters(), lr=0.3)

# 权重衰减的简洁实现
# trainer = torch.optim.SGD([
#     {"params": net[0].weight, 'weight_decay': wd},
#     {"params": net[0].bias}
# ], lr=lr)

# 暂退法 (Dropout)
X = torch.tensor([0.1, 0.2, 0.3, 0.4])
dropout = 0.5
# 可以直接用比较生成一个相同大小的 bool tensor
mask = (torch.rand(X.shape) > dropout).float()
print(mask)
print(X)
print(mask * X / (1.0 - dropout))
```

### 4.4 自定义块与 Sequential

- 继承 `torch.nn.Module` 定义自定义块
- `MySequential` 使用自带的 `_modules` 列表，方便参数初始化

```python
# 自定义块
class MLP(torch.nn.Module):  # 继承 torch.nn.Module
    def __init__(self):
        super().__init__()
        self.hidden = torch.nn.Linear(20, 256)
        self.out = torch.nn.Linear(256, 10)

    def forward(self, X):
        return self.out(torch.nn.functional.relu(self.hidden(X)))

# 顺序块 Sequential
class MySequential(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()
        for idx, module in enumerate(args):
            # 使用自带的 _modules 列表，而不是自己定义一个，方便参数的初始化
            self._modules[str(idx)] = module

    def forward(self, X):
        for block in self._modules.values():
            X = block(X)
        return X

print()
```

### 4.5 参数访问、嵌套与初始化

```python
# 访问 Sequential 的所有参数
print([(name, param) for name, param in net.named_parameters()])

# 模块嵌套，并访问参数
net = torch.nn.Sequential(torch.nn.Sequential(
    torch.nn.Linear(20, 256), torch.nn.ReLU(), torch.nn.Linear(256, 10)))
# 要有第一个参数，用来指定名字
net.add_module(f'block{1}', torch.nn.Sequential(
    torch.nn.Linear(20, 256), torch.nn.ReLU(), torch.nn.Linear(256, 10)))

# 参数初始化
def init_normal(m):
    if type(m) == torch.nn.Linear:
        torch.nn.init.normal_(m.weight, mean=0., std=0.01)
        torch.nn.init.zeros_(m.bias)

net.apply(init_normal)

# Xavier 初始化
def init_xavier(m):
    if type(m) == torch.nn.Linear:
        torch.nn.init.xavier_uniform_(m.weight)
```

### 4.6 自定义层与模型保存/加载

```python
# 自定义层
class CenteredLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X - X.mean()

layer = CenteredLayer()
print(layer(torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)),
      layer(torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)).mean())

# 模型保存
# torch.save(net.state_dict(), './Python/Learning/Deep_Learn/net.pth')
# 模型加载，网络要先定义好
# net.load_state_dict(torch.load('./Python/Learning/Deep_Learn/net.pth'))
```

### 4.7 卷积与 BatchNorm 片段

这部分在 MLP 学习文件中作为片段出现，完整卷积内容见[第 5 节](#5-卷积神经网络)。

```python
X = torch.arange(9.0).reshape(3, 3)
print(X.shape)
X = X.reshape((1, 1) + X.shape)
print(X.shape)
print(X)

def corr2d(X, K):
    h, w = K.shape
    Y = torch.zeros(X.shape[0] - h + 1, X.shape[1] - w + 1)
    for i in range(Y.shape[0]):
        for j in range(X.shape[1]):
            Y[i, j] = (X[i:i + h, j:j + w] * K).sum()
    return Y

def corr2d_multi_in(X, K):
    return sum(corr2d(x, k) for x, k in zip(X, K))

def corr2d_multi_in_out(X, K):
    return torch.stack([corr2d_multi_in(X, k) for k in K], 0)

X = torch.normal(0, 1, (3, 3, 3))
K = torch.normal(0, 1, (2, 3, 1, 1))
Y1 = corr2d_multi_in_out(X, K)
print(Y1.shape)
print(Y1)
print()

def pool2d(X, pool_size, mode='max'):
    p_h, p_w = pool_size
    Y = torch.zeros(X.shape[0] - p_h + 1, X.shape[1] - p_w + 1)
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode == 'max':
                Y[i, j] = X[i:i + p_h, j:j + p_w].max()
            elif mode == 'avg':
                Y[i, j] = X[i:i + p_h, j:j + p_w].mean()
    return Y
```

```python
import torch.nn as nn

def batch_norm(X, gamma, beta, moving_mean, moving_var, eps, momentum):
    if not torch.is_grad_enabled():
        X_hat = (X - moving_mean) / torch.sqrt(moving_var + eps)
    else:
        assert len(X.shape) in (2, 4)
        if len(X.shape) == 2:
            mean = X.mean(dim=0)
            var = ((X - mean) ** 2).mean(dim=0)
        else:
            mean = X.mean(dim=(0, 2, 3), keepdim=True)
            var = ((X - mean) ** 2).mean(dim=(0, 2, 3), keepdim=True)
        X_hat = (X - mean) / torch.sqrt(var + eps)
        moving_mean = momentum * moving_mean + (1.0 - momentum) * mean
        moving_var = momentum * moving_var + (1.0 - momentum) * var
    Y = gamma * X_hat + beta
    return Y, moving_mean, moving_var
```

```python
# 文本 token 化片段
lines = ['hello world', 'hello deep learning']

print([line.split() for line in lines])
print([list(line) for line in lines])

print(isinstance([line.split() for line in lines][0], list))
# print(count_corpus([line.split() for line in lines]))
```

## 5 卷积神经网络

来源：`A6.py`、`A6-6._LeNet.py` — 二维卷积从零实现、填充/步幅、多通道、1×1 卷积、汇聚层、LeNet。

卷积操作（互相关）：$Y[i,j] = \sum_{a,b} X[i+a, j+b] \cdot K[a, b]$

### 5.1 二维卷积与学习卷积核

- `corr2d` 从零实现互相关运算
- 通过反向传播学习卷积核
- 填充 `padding` 控制输出形状
- 步幅 `stride` 控制输出形状

```python
# 卷积核
import torch
from d2l import torch as d2l
from torch import nn

def comp_conv2d(conv2d, X):
    # 前两个 1 表示：批量大小和维度
    X = X.reshape((1, 1) + X.shape)
    Y = conv2d(X)
    # 返回时忽略前两个维度
    return Y.reshape(Y.shape[2:])

X = torch.rand(size=(8, 8))
# 填充
conv2d = nn.Conv2d(1, 1, kernel_size=(5, 3), padding=(2, 1))
print(comp_conv2d(conv2d, X).shape)

# 步幅
conv2d = nn.Conv2d(1, 1, kernel_size=(3, 5), padding=(0, 1), stride=(3, 4))
print(comp_conv2d(conv2d, X).shape)
```

### 5.2 多通道输入与输出

- `corr2d_multi_in`：多输入通道，对每个通道分别做互相关再求和
- `corr2d_multi_in_out`：多输出通道，堆叠多个核的结果
- 1×1 卷积等价于全连接层的矩阵乘法

```python
# 多通道输入
def corr2d_multi_in(X, K):
    return sum(d2l.corr2d(x, k) for x, k in zip(X, K))

X = torch.tensor([[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],
               [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]])
K = torch.tensor([[[0.0, 1.0], [2.0, 3.0]], [[1.0, 2.0], [3.0, 4.0]]])

print(corr2d_multi_in(X, K))

# 多通道输出
def corr2d_multi_in_out(X, K):
    # 迭代 K 的第 0 个维度，每次都对输入 X 执行互相关运算。
    # 最后将所有结果都叠加在一起
    return torch.stack([corr2d_multi_in(X, k) for k in K], 0)

K = torch.stack((K, K + 1, K + 2), 0)
print(K.shape)
print(corr2d_multi_in_out(X, K))

# 1*1 卷积
def corr2d_multi_in_out_1x1(X, K):
    c_i, h, w = X.shape
    c_o = K.shape[0]
    X = X.reshape((c_i, h * w))
    K = K.reshape((c_o, c_i))
    # 全连接层中的矩阵乘法
    Y = torch.matmul(K, X)
    return Y.reshape((c_o, h, w))

X = torch.normal(0, 1, (3, 3, 3))
K = torch.normal(0, 1, (2, 3, 1, 1))
Y1 = corr2d_multi_in_out_1x1(X, K)
Y2 = corr2d_multi_in_out(X, K)
assert float(torch.abs(Y1 - Y2).sum()) < 1e-6
```

### 5.3 汇聚层（池化）

- 最大汇聚 `max`、平均汇聚 `avg`
- `nn.MaxPool2d` 的简洁实现

```python
def pool2d(X, pool_size, mode='max'):
    p_h, p_w = pool_size
    Y = torch.zeros((X.shape[0] - p_h + 1, X.shape[1] - p_w + 1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode == 'max':
                Y[i, j] = X[i: i + p_h, j: j + p_w].max()
            elif mode == 'avg':
                Y[i, j] = X[i: i + p_h, j: j + p_w].mean()
    return Y

X = torch.tensor([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]])
print(pool2d(X, (2, 2)))
print(pool2d(X, (2, 2), 'avg'))

X = torch.arange(16, dtype=torch.float32).reshape((1, 1, 4, 4))

pool2d = nn.MaxPool2d(3)
print(pool2d(X))

pool2d = nn.MaxPool2d((2, 3), stride=(2, 3), padding=(0, 1))
print(pool2d(X))
```

### 5.4 LeNet

经典 LeNet 结构：

```
Conv(1→6, 5×5, pad=2) → Sigmoid → MaxPool(2×2)
→ Conv(6→16, 5×5) → Sigmoid → MaxPool(2×2)
→ Flatten → Linear(16*5*5→120) → Sigmoid
→ Linear(120→84) → Sigmoid → Linear(84→10)
```

在 Fashion-MNIST 上训练。

```python
# LeNet
import torch
from torch import nn
from d2l import torch as d2l

net = nn.Sequential(
    nn.Conv2d(1, 6, kernel_size=5, padding=2), nn.Sigmoid(),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Conv2d(6, 16, kernel_size=5), nn.Sigmoid(),
    nn.MaxPool2d(kernel_size=2, stride=2),
    nn.Flatten(),
    nn.Linear(16 * 5 * 5, 120), nn.Sigmoid(),
    nn.Linear(120, 84), nn.Sigmoid(),
    nn.Linear(84, 10))

# X = torch.rand(size=(1, 1, 28, 28), dtype=torch.float32)
# for layer in net:
#     X = layer(X)
#     print(layer.__class__.__name__, 'output shape: \t', X.shape)

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size=batch_size)

lr, num_epochs = 0.6, 20
d2l.train_ch6(net, train_iter, test_iter, num_epochs, lr, d2l.try_gpu())
d2l.plt.show()
```

## 6 循环神经网络与时间序列

来源：`A8-1.py`、`A8-5.py`、`A9-1.py` — GRU 从零实现、GRU 简洁实现、时间序列预测。

GRU 的核心是两个门：
- **更新门** $Z = \sigma(X W_{xz} + H W_{hz} + b_z)$，控制保留多少历史状态
- **重置门** $R = \sigma(X W_{xr} + H W_{hr} + b_r)$，控制如何将历史状态与当前输入结合
- **候选状态** $\tilde{H} = \tanh(X W_{xh} + (R \odot H) W_{hh} + b_h)$
- **新状态** $H = Z \odot H + (1-Z) \odot \tilde{H}$

### 6.1 GRU 从零实现

包括 `get_params`、`init_gru_state`、`gru` 前向传播，使用时间机器数据训练。

```python
# 门控循环单元
import torch
from torch import nn
from d2l import torch as d2l

batch_size, num_steps = 32, 35
train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)

def get_params(Vocab_size, num_hiddens, device):
    num_inputs = num_outputs = Vocab_size

    def normal(shape):
        return torch.randn(size=shape, device=device) * 0.01

    def three():
        return (normal((num_inputs, num_hiddens)),
                normal((num_hiddens, num_hiddens)),
                torch.zeros(num_hiddens, device=device))

    W_xz, W_hz, b_z = three()
    W_xr, W_hr, b_r = three()
    W_xh, W_hh, b_h = three()

    W_hq = normal((num_hiddens, num_outputs))
    b_q = torch.zeros(num_outputs, device=device)

    params = [W_xz, W_hz, b_z, W_xr, W_hr, b_r, W_xh, W_hh, b_h, W_hq, b_q]
    for param in params:
        param.requires_grad_(True)
    return params

def init_gru_state(batch_size, num_hiddens, device):
    return (torch.zeros((batch_size, num_hiddens), device=device), )

def gru(inputs, state, params):
    W_xz, W_hz, b_z, W_xr, W_hr, b_r, W_xh, W_hh, b_h, W_hq, b_q = params
    H, = state
    outputs = []
    for X in inputs:
        Z = torch.sigmoid((X @ W_xz) + (H @ W_hz) + b_z)
        R = torch.sigmoid((X @ W_xr) + (H @ W_hr) + b_r)
        H_tilda = torch.tanh((X @ W_xh) + ((R * H) @ W_hh) + b_h)
        H = Z * H + (1 - Z) * H_tilda
        Y = H @ W_hq + b_q
        outputs.append(Y)
    return torch.cat(outputs, dim=0), (H,)

vocal_size, num_hiddens, device = len(vocab), 256, d2l.try_gpu()
num_epochs, lr = 500, 1
model = d2l.RNNModelScratch(len(vocab), num_hiddens, device, get_params,
                            init_gru_state, gru)
d2l.train_ch8(model, train_iter, vocab, lr, num_epochs, device)

d2l.plt.show()
```

### 6.2 GRU 简洁实现

使用 `nn.GRU` + `RNNModel`。

```python
import torch
from torch import nn
from d2l import torch as d2l

batch_size, num_steps = 32, 35
train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)

num_epochs, lr = 500, 1
device = d2l.try_gpu()
loss = nn.CrossEntropyLoss()
gru_layer = nn.GRU(input_size=len(vocab), hidden_size=256)
model = d2l.RNNModel(gru_layer, len(vocab))
d2l.train_ch8(model, train_iter, vocab, lr, num_epochs, device)
```

### 6.3 时间序列预测

使用正弦波数据 $x = \sin(0.01 t) + \epsilon$ 进行自回归建模。

- **单步预测**：使用真实历史数据预测下一个时间步
- **多步预测**：使用模型自身的预测作为输入继续预测，误差会累积
- **k 步预测**：分析不同预测步数的偏差

```python
import torch
from torch import nn
from d2l import torch as d2l

T = 1000
time = torch.arange(1, 1 + T, dtype=torch.float32)
x = torch.sin(0.01 * time) + torch.normal(0, 0.2, (T,))
d2l.plot(time, [x], 'time', 'x', xlim=[1, 1000], figsize=(6, 3))
# d2l.plt.show()

tau = 4
features = torch.zeros(T - tau, tau)
for i in range(tau):
    features[:, i] = x[i:i + T - tau]
labels = x[tau:].reshape((-1, 1))

batch_size, n_train = 16, 600
train_iter = d2l.load_array((features[:n_train], labels[:n_train]),
                              batch_size, is_train=True)

def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.xavier_uniform_(m.weight)

def get_net():
    net = nn.Sequential(nn.Linear(4, 10), nn.ReLU(), nn.Linear(10, 1))
    net.apply(init_weights)
    return net

loss = nn.MSELoss(reduction='none')

def train(net, train_iter, loss, epochs, lr):
    trainer = torch.optim.Adam(net.parameters(), lr)
    for epoch in range(epochs):
        for X, y in train_iter:
            trainer.zero_grad()
            l = loss(net(X), y)
            l.sum().backward()
            trainer.step()
        print(f'epoch {epoch + 1}, '
              f'loss: {d2l.evaluate_loss(net, train_iter, loss):f}')

net = get_net()
train(net, train_iter, loss, 10, 0.01)
```

```python
# 单步预测
onestep_preds = net(features)
# 使用原始数据，对下一个时间步进行预测
d2l.plot([time, time[tau:]],
        [x.detach().numpy(), onestep_preds.detach().numpy()],
        'time', 'x', legend=['data', '1-step preds'],
        xlim=[1, 1000], figsize=(6, 3))
# d2l.plt.show()

# 多步预测
multistep_preds = torch.zeros(T)
multistep_preds[:n_train + tau] = x[:n_train + tau]
for i in range(n_train + tau, T):
    multistep_preds[i] = net(multistep_preds[i - tau:i].reshape((1, -1)))

d2l.plot([time, time[tau:], time[n_train + tau:]],
        [x.detach().numpy(), onestep_preds.detach().numpy(),
         multistep_preds[n_train + tau:].detach().numpy()],
        'time', 'x', legend=['data', '1-step preds', 'multistep preds'],
        xlim=[1, 1000], figsize=(6, 3))
# d2l.plt.show()
```

```python
# k 步预测
max_steps = 64
features = torch.zeros((T - tau - max_steps + 1, tau + max_steps))
for i in range(tau):
    features[:, i] = x[i:i + T - tau - max_steps + 1]

for i in range(tau, tau + max_steps):
    features[:, i] = net(features[:, i - tau:i]).reshape(-1)

steps = (1, 4, 16, 64)
d2l.plot([time[tau + i - 1:T - max_steps + i] for i in steps],
        [features[:, (tau + i - 1)].detach().numpy() for i in steps],
        'time', 'x', legend=[f'{i}-step preds' for i in steps],
        xlim=[5, 1000], figsize=(6, 3))

d2l.plt.show()
```

## 7 概率基础

来源：`temp3.py` — 多项分布采样。

```python
# 概率
import torch
from torch.distributions import multinomial

fair_ = torch.ones([6]) / 6
print(multinomial.Multinomial(100000, fair_).sample())
```

## 8 草稿与实验

来源：`temp.py`、`temp2.py` — 综合实验草稿，包含被注释掉的实验片段。

> 注：这些是学习过程中的草稿代码，部分函数有拼写错误（原文件保留），仅供参考。

### 8.1 综合草稿（temp.py）

包含自动微分、MLP、Sequential、参数初始化、卷积核学习、时间序列、梯度下降、分块矩阵乘法计时等片段。

```python
import math

import torch
from d2l import torch as d2l

# x = torch.arange(12.0, requires_grad=True)
# y = 10 * torch.dot(x, x)
# n = torch.arange(3.0, requires_grad=True)
# z = 10 * n * n
# y.backward()
# z.backward(torch.ones_like(torch.ones(z.shape)))
# print(x.grad)
# print(n.grad)
# print(x.grad == n.grad)

# y = torch.matmul(x.reshape(6, 2), torch.tensor([1.0, 2.0]))
# print(y)
# x.grad.zero_()
# y = x * x
# u = y.detach()
# z = u * x
# z.sum().backward()
# print(x.grad)

# x = torch.arange(-8.0, 8.0, 0.1, requires_grad=True)
# y = torch.relu(x)
# d2l.plot(x.detach(), y.detach(), 'x', 'relu(x)', figsize=(5, 2.5))

# M = torch.normal(0, 1, size=(4, 4))
# print(M)
# for i in range(100):
#     M = torch.mm(M, torch.normal(0, 1, size=(4, 4)))
# print(M)

# y = torch.tensor([0, 2])
# y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5]])
# print(-torch.log(y_hat[range(len(y_hat)), y]))

# from torch import nn
# from torch.nn import functional as F
#
# net = nn.Sequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
# X = torch.rand(2, 20)
# print(net(X))

# class MLP(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.hidden = nn.Linear(20, 256)
#         self.out = nn.Linear(256, 10)
#     def forward(self, X):
#         return self.out(F.relu(self.hidden(X)))
#
# net = MLP()
# print(net(X))

# def init_normal(m):
#     if type(m) == nn.linear:
#         nn.init.normal(m.weight, mean=0, std=0.01)
#         nn.init.zeros_(m.bias)
# net.apply(init_normal)

# x = torch.arange(4)
# torch.save(x, "x-file")
# x2 = torch.load('x-file')
# print(x2)

# net = MLP()
# X = torch.randn(size=(2, 20))
# Y = net(X)
# torch.save(net.state_dict(), 'mlp.params')
# clone = MLP()
# clone.load_state_dict(torch.load('mlp.params'))
# clone.eval()
# Y_clone = clone(X)
# print(Y_clone == Y)

# print(d2l.try_gpu())
# x = torch.tensor(4)
# print(x.device)

# def corr2d(X, K):
#     h, w = K.shape
#     Y = torch.zeros((X.shape[0] - h + 1), (X.shape[1] - w + 1))
#     for i in range(Y.shape[0]):
#         for j in range(Y.shape[1]):
#             Y[i, j] = (X[i:i + h, j:j + w] * K).sum()
#     return Y

# T = 1000
# time = torch.arange(1, T + 1, dtype=torch.float32)
# x = torch.sin(0.01 * time) + torch.normal(0, 0.2, (T,))
# tau = 4
# features = torch.zeros((T - tau, tau))
# for i in range(tau):
#     features[:, i] = x[i: T - tau + i]
# labels = x[tau:].reshape((-1, 1))

# def f(x):
#     return x ** 2
# def f_grad(x):
#     return 2 * x
# def gd(eta, f_grad):
#     x = 10.0
#     results = [x]
#     for i in range(20):
#         x -= eta * f_grad(x)
#         results.append(x)
#     print('epoch 10, x:', x)
#     return results
# res = gd(0.2, f_grad)
# print(res)

# 分块矩阵乘法计时
timer = d2l.Timer()
A = torch.zeros((256, 256))
B = torch.randn((256, 256))
C = torch.randn((256, 256))
timer.start()
for j in range(0, 256, 64):
    A[:, j:j + 64] = torch.mm(B, C[:, j:j + 64])
timer.stop()
print(f'{timer.times[0]:.5f} sec')
print(A)
```

### 8.2 早期线性回归草稿（temp2.py）

> ⚠️ 原文件存在拼写错误（`batch.size`、`param.grad_zero_()`、`toech.nn.Linear`），这里按原样保留作为学习记录。

```python
# import torch
# from d2l import torch as d2l
# import random
#
# X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
# X[1, 2] = 9
# print(X)
# a = [[1, 2, 3], [4, 5, 6]]
# a[1][2] = 9
# print(a)
#
# # 内存是否重新分配
# Y = X.clone()
# print(id(Y))
# Y = Y + X
# print(id(Y))
# Y[:] = X + Y
# print(id(Y))
#
# # 线性代数
# X = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
# Y = torch.tensor([[10.0, 20.0], [30.0, 40.0]])
# print(X.mean(), X.sum() / X.numel())
#
# # 自动微分（只能计算在某一个值的导数）
# X = torch.arange(4.0, requires_grad=True)
# Y = X * X
# Y.sum().backward()
# print(X.grad)
#
# # 分离计算
# X.grad.zero_()
# Y = X * X
# U = Y.detach()
# Z = U * X
# Z.sum().backward()
# print(X.grad)

# 小批量抽样
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = indices[i:min(i + batch_size, num_examples)]
        yield features[batch_indices], labels[batch_indices]

import torch
import random

f = torch.tensor([2, 3, 4, 5])
l = torch.tensor([1, 2, 3, 4])
for x, y in data_iter(2, f, l):
    print(x, y)

# 小批量随机梯度下降（注意：原文件有拼写错误，此处按原样保留）
# def sgd(params, lr, batch_size):
#     with torch.no_grad():
#         for param in params:
#             param -= lr * param.grad / batch.size          # batch.size 应为 batch_size
#             param.grad_zero_()                              # 应为 grad.zero_()

net = torch.nn.Sequential(torch.nn.Linear(2, 1))
net[0].weight.data.normal_(0, 0.01)
net[0].bias.data.fill_(0)
loss = torch.nn.MSELoss()
trainer = torch.optim.SGD(net.parameters(), lr=0.3)

# 权重衰减的简洁实现
# trainer = torch.optim.SGD([
#     {"params": net[0].weight, 'weight_decay': wd},
#     {"params": net[0].bias}
# ], lr=lr)

# 暂退法
X = torch.tensor([0.1, 0.2, 0.3, 0.4])
dropout = 0.5
mask = (torch.rand(X.shape) > dropout).float()
print(mask)
print(X)
print(mask * X / (1.0 - dropout))

# 自定义块（注意：原文件 toech.nn.Linear 为拼写错误）
# class MLP(torch.nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.hidden = toech.nn.Linear(20, 256)   # toech 应为 torch
#         self.out = torch.nn.Linear(256, 10)
#     def forward(self, X):
#         return self.out(torch.functional.relu(self.hidden(X)))

# 顺序块 Sequential
class MySequential(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()
        for idx, module in enumerate(args):
            self._modules[str(idx)] = module

    def forward(self, X):
        for block in self._modules.values():
            X = block(X)
        return X
print()

# 访问 Sequential 的所有参数
print([(name, param) for name, param in net.named_parameters()])
net = torch.nn.Sequential(torch.nn.Sequential(
    torch.nn.Linear(20, 256), torch.nn.ReLU(), torch.nn.Linear(256, 10)))
net.add_module(f'block{1}', torch.nn.Sequential(
    torch.nn.Linear(20, 256), torch.nn.ReLU(), torch.nn.Linear(256, 10)))

# 参数初始化
def init_normal(m):
    if type(m) == torch.nn.Linear:
        torch.nn.init.normal_(m.weight, mean=0., std=0.01)
        torch.nn.init.zeros_(m.bias)

net.apply(init_normal)

def init_xavier(m):
    if type(m) == torch.nn.Linear:
        torch.nn.init.xavier_uniform_(m.weight)

# 自定义层
class CenteredLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, X):
        return X - X.mean()

layer = CenteredLayer()
print(layer(torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)),
      layer(torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)).mean())

# 模型保存/加载
# torch.save(net.state_dict(), './Python/Learning/Deep_Learn/net.pth')
# net.load_state_dict(torch.load('./Python/Learning/Deep_Learn/net.pth'))

X = torch.arange(9.0).reshape(3, 3)
print(X.shape)
X = X.reshape((1, 1) + X.shape)
print(X.shape)
print(X)
```

### 8.3 简单卷积测试（temp3.py 之前的内容）

使用 `torch.conv2d` 进行简单的卷积运算测试。

```python
import torch
from d2l import torch as d2l
x = torch.arange(20).reshape((1, 1, 4, 5))
y = torch.arange(4).reshape((1, 1, 2, 2))
z = torch.conv2d(x, y)
print(z)
```
