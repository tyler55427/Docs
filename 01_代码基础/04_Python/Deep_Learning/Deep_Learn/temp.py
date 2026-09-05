import math

import torch
from d2l import torch as d2l

# x=torch.arange(12.0,requires_grad=True)
# y=10*torch.dot(x,x)
# n=torch.arange(3.0,requires_grad=True)
# z=10*n*n
# # y = x*x
# y.backward()
# z.backward(torch.ones_like(torch.ones(z.shape)))
# print(x.grad)
# print(n.grad)
# print(x.grad==n.grad)

# y=torch.matmul(x.reshape(6,2),torch.tensor([1.0,2.0]))
# print(y)
# x.grad.zero_()
# y = x*x
# u = y.detach()
# z = u*x
# z.sum().backward()
# print(x.grad)

# x = torch.arange(-8.0,8.0,0.1,requires_grad=True)
# y = torch.relu(x)
# d2l.plot(x.detach(),y.detach(),'x','relu(x)',figsize=(5,2.5))
#
# M = torch.normal(0,1,size=(4,4))
# print(M)
# for i in range(100):
#     M = torch.mm(M,torch.normal(0,1,size=(4,4)))
# print(M)

# y = torch.tensor([0,2])
# y_hat = torch.tensor([[0.1,0.3,0.6],[0.3,0.2,0.5]])
# print(-torch.log(y_hat[range(len(y_hat)),y]))

import torch
from torch import nn
from torch.nn import functional as F

# net = nn.Sequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
#
# X = torch.rand(2, 20)
# print(net(X))

# class MLP(nn.Module):
#     # 用模型参数声明层。这里，我们声明两个全连接的层
#     def __init__(self):
#         # 调用MLP的父类Module的构造函数来执行必要的初始化。
#         # 这样，在类实例化时也可以指定其他函数参数，例如模型参数params（稍后将介绍）
#         super().__init__()
#         self.hidden = nn.Linear(20, 256)  # 隐藏层
#         self.out = nn.Linear(256, 10)  # 输出层
#
#     # 定义模型的前向传播，即如何根据输入X返回所需的模型输出
#     def forward(self, X):
#         # 注意，这里我们使用ReLU的函数版本，其在nn.functional模块中定义。
#         return self.out(F.relu(self.hidden(X)))
#
# net = MLP()
# print(net(X))

# def init_normal(m):
#     if type(m)==nn.linear:
#         nn.init.normal(m.weight,mean=0,std=0.01)
#         nn.init.zeros_(m.bias)
# net.apply(init_normal)

# class MLP(nn.Module):
#     # def __init__(self,in_n,out_n):
#     def __init__(self):
#         super().__init__()
#         # self.weight = nn.Parameter(torch.randn(in_n,out_n))
#         # self.bias = nn.Parameter(torch.randn(out_n,))
#
#     def forward(self,X):
#         # linear = torch.matmul(X,self.weight.data) + self.bias.data
#         # return F.relu(linear)
#         return X-X.mean()
#
# linear = MLP(5,3)
# print(linear.weight)

# x = torch.arange(4)
# torch.save(x,"x-file")

# x2 = torch.load('x-file')
# print(x2)


# net = MLP()
# X = torch.randn(size=(2,20))
# Y = net(X)
# torch.save(net.state_dict(),'mlp.params')
#
# clone = MLP()
# clone.load_state_dict(torch.load('mlp.params'))
# clone.eval()
#
# Y_clone = clone(X)
# print(Y_clone==Y)

# print(d2l.try_gpu())
# x = torch.tensor(4)
# print(x.device)

# def corr2d(X,K):
#     h,w = K.shape
#     Y = torch.zeros((X.shape[0]-h+1),(X.shape[1]-w+1))
#     for i in range(Y.shape[0]):
#         for j in range(Y.shape[1]):
#             Y[i,j] = (X[i:i+h,j:j+w]*K).sum()
#     return Y
#
# # X = torch.tensor([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]])
# # K = torch.tensor([[0.0, 1.0], [2.0, 3.0]])
# # Y = corr2d(X,K)
#
# X = torch.ones((6,8))
# X[:,2:6] = 0
# K = torch.tensor([1.0,-1.0]).reshape((1,2))
# Y = corr2d(X,K)
#
# # 构造一个二维卷积层，它具有1个输出通道和形状为（1，2）的卷积核
# conv2d = nn.Conv2d(1,1, kernel_size=(1, 2), bias=False)
#
# # 这个二维卷积层使用四维输入和输出格式（批量大小、通道、高度、宽度），
# # 其中批量大小和通道数都为1
# X = X.reshape((1, 1, 6, 8))
# Y = Y.reshape((1, 1, 6, 7))
# lr = 3e-2  # 学习率
#
# for i in range(10):
#     Y_hat = conv2d(X)
#     l = (Y_hat - Y) ** 2
#     conv2d.zero_grad()
#     l.sum().backward()
#     # 迭代卷积核
#     conv2d.weight.data[:] -= lr * conv2d.weight.grad
#     if (i + 1) % 2 == 0:
#         print(f'epoch {i+1}, loss {l.sum():.3f}')
#
# print(conv2d.weight.data.reshape(1,2))


# T = 1000  # 总共产生1000个点
# time = torch.arange(1, T + 1, dtype=torch.float32)
# x = torch.sin(0.01 * time) + torch.normal(0, 0.2, (T,))
# print(x)

# tau = 4
# features = torch.zeros((T - tau, tau))
# for i in range(tau):
#     features[:, i] = x[i: T - tau + i]
# labels = x[tau:].reshape((-1, 1))

# print(features)
# print(labels)

# def f(x):
#     return x**2

# def f_grad(x):
#     return 2*x

# def gd(eta,f_grad):
#     x = 10.0
#     results = [x]
#     for i in range(20):
#         x -= eta * f_grad(x)
#         results.append(x)
#     print('epoch 10, x:', x)
#     return results

# res = gd(0.2,f_grad)
# print(res)

timer = d2l.Timer()
A = torch.zeros((256,256))
B = torch.randn((256,256))
C = torch.randn((256,256))
timer.start()
for j in range(0,256,64):
    A[:,j:j+64] = torch.mm(B,C[:,j:j+64])
timer.stop()
print(f'{timer.times[0]:.5f} sec')
print(A)
