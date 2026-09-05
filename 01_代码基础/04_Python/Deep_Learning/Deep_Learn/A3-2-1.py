# 线性神经网络

import math
import numpy as np
import torch
import random
from d2l import torch as d2l


# 正态分布
def normal(x,mu,sigma):
    p=1/math.sqrt(2*math.pi*sigma**2)
    return p*np.exp(-0.5/sigma**2*(x-mu)**2)

w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# def plot_ZhengTai():
#     x = np.arange(-7, 7, 0.01)
#     params = [(0, 1), (0, 2), (3, 1)]
#     d2l.plot(x, [normal(x, mu, sigma) for mu, sigma in params], xlabel='x', ylabel='p(x)', figsize=(4.5, 2.5),
#              legend=[f'mean{mu},std{sigma}' for mu, sigma in params])
#     d2l.plt.show()

# 线性回归的底层代码

# 生成数据集
def synthetic_data(w,b,num_examples):
    X=torch.normal(0,1,(num_examples,len(w)))
    y=torch.matmul(X,w)+b
    y+=torch.normal(0,0.01,y.shape)
    return X,y.reshape((-1,1))

true_w=torch.tensor([2,-3.4])
true_b=4.2
features, labels = synthetic_data(true_w,true_b,1000)


# 打乱并小批量获取数据集的样本
def data_iter(batch_size,features,labels):
    num_examples=len(features)
    indices=list(range(num_examples))
    random.shuffle(indices)
    for i in range(0,num_examples,batch_size):
        batch_indices=torch.tensor(
            indices[i:min(i+batch_size,num_examples)])
        yield features[batch_indices],labels[batch_indices]

batch_size=10
# for X,y in data_iter(batch_size,features,labels):
#     print(X,'\n',y)
#     break

def linreg(X,w,b):
    # 线性回归模型
    return torch.matmul(X,w)+b

def squared_loss(y_hat,y):
    # 均方损失
    return (y_hat-y.reshape(y_hat.shape))**2/2

def sgd(params,lr,batch_size):
    # 小批量随机梯度下降
    with torch.no_grad():
        for param in params:
            param -= lr*param.grad/batch_size
            param.grad.zero_()

# 开始训练
lr=0.03
num_epochs=3
net=linreg
loss=squared_loss

for epoch in range(num_epochs):
    for X,y in data_iter(batch_size,features,labels):
        l=loss(net(X,w,b),y)
        l.sum().backward()
        sgd([w,b],lr,batch_size)
    with torch.no_grad():
        train_l=loss(net(features,w,b),labels)
        print(f'epoch{epoch+1},loss{float(train_l.mean()):f}')
