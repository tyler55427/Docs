# 卷积核
import torch
from d2l import torch as d2l
from torch import nn

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

def comp_conv2d(conv2d,X):
    # 前两个1表示：批量大小和维度
    X = X.reshape((1,1)+X.shape)
    Y = conv2d(X)
    # 返回时忽略前两个维度
    return Y.reshape(Y.shape[2:])

X = torch.rand(size=(8,8))
# 填充
conv2d = nn.Conv2d(1,1,kernel_size=(5,3),padding=(2,1))
print(comp_conv2d(conv2d,X).shape)

# 步幅
conv2d = nn.Conv2d(1,1,kernel_size=(3,5),padding=(0,1),stride=(3,4))
print(comp_conv2d(conv2d, X).shape)


# 多通道输入
def corr2d_multi_in(X,K):
    return sum(d2l.corr2d(x,k) for x,k in zip(X,K))

X = torch.tensor([[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]],
               [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]])
K = torch.tensor([[[0.0, 1.0], [2.0, 3.0]], [[1.0, 2.0], [3.0, 4.0]]])

print(corr2d_multi_in(X, K))

# 多通道输出

def corr2d_multi_in_out(X, K):
    # 迭代“K”的第0个维度，每次都对输入“X”执行互相关运算。
    # 最后将所有结果都叠加在一起
    return torch.stack([corr2d_multi_in(X, k) for k in K], 0)

K = torch.stack((K, K + 1, K + 2), 0)
print(K.shape)
print(corr2d_multi_in_out(X, K))


# 1*1卷积

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


# 汇聚层

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