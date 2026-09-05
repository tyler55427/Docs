import torch
from d2l import torch as d2l
import random

X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
X[1,2] = 9
print(X)
# 和python不同的取值方式
a = [[1,2,3],[4,5,6]]
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
print(X.mean(), X.sum()/X.numel())

# 自动微分（只能计算在某一个值的导数）
X = torch.arange(4.0,requires_grad=True)
Y = X*X
# 只有输出是scalar（标量），才能无参数调用，否则要传入一个gradient参数，指定微分函数关于self的梯度
# 等价于 Y.backward(torch.ones(len(X)))
Y.sum().backward()
print(X.grad)
print()


# 分离计算
X.grad.zero_()
Y = X*X
# 将Y作为常数分离出来，不参与X的反向微分计算
U = Y.detach()
Z = U*X
Z.sum().backward()
print(X.grad)
# 二阶导数应该怎么求？


# 小批量抽样
def data_iter(batch_size,features,labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0,num_examples,batch_size):
        batch_indices = indices[i:min(i+batch_size,num_examples)]
        yield features[batch_indices], labels[batch_indices]


f = torch.tensor([2,3,4,5])
l = torch.tensor([1,2,3,4])
# 传入的是tensor，不是list
# tensor可以通过列表索引来生成新的tensor
for x,y in data_iter(2,f,l):
    print(x,y)


# 小批量随机梯度下降
def sgd(params,ls,batch_size):
    with torch.no_grad():
        for param in params:
            # 每个参数都有一个梯度，它们是不同的
            # 关于不同参数的有不同的偏导，它们的梯度是分开计算的
            param -= lr * param.grad / batch.size
            param.grad_zero_()

net = torch.nn.Sequential(torch.nn.Linear(2,1))
net[0].weight.data.normal_(0,0.01)
net[0].bias.data.fill_(0)
loss = torch.nn.MSELoss()
trainer = torch.optim.SGD(net.parameters(),lr=0.3)


# 权重衰减的简洁实现
# trainer = torch.optim.SGD([
#     {"params":net[0].weight,'weight_decay':wd},
#     {"params":net[0].bias}
# ],lr=lr)   

# 暂退法
X=torch.tensor([0.1,0.2,0.3,0.4])
dropout=0.5
# 可以直接用比较生成一个相同大小的bool tensor
mask = (torch.rand(X.shape)>dropout).float()
print(mask)
print(X)
print(mask*X/(1.0-dropout))

# 自定义块
class MLP(torch.nn.Module): # 继承torch.nn.Module
    def __init__(self):
        super().__init__()
        self.hidden = toech.nn.Linear(20,256)
        self.out = torch.nn.Linear(256,10)

    def forward(self,X):
        return self.out(torch.functional.relu(self.hidden(X)))

# 顺序快Sequential
class MySequential(torch.nn.Module):
    def __init__(self,*args):
        super().__init__()
        for idx,module in enumerate(args):
            # 使用自带的_modules列表，而不是自己定义一个，方便参数的初始化
            self._modules[str(idx)]=module
        
    def forward(self,X):
        for block in self._modules.values():
            X = block(X)
        return X
print()

# 访问Sequential的所有参数
print([(name,param) for name,param in net.named_parameters()])
# 模块嵌套，并访问参数
net = torch.nn.Sequential(torch.nn.Sequential(torch.nn.Linear(20,256),torch.nn.ReLU(),torch.nn.Linear(256,10)))
# 要有第一个参数，用来指定名字
net.add_module(f'block{1}',torch.nn.Sequential(torch.nn.Linear(20,256),torch.nn.ReLU(),torch.nn.Linear(256,10)))

# 参数初始化
def init_normal(m):
    if type(m)==torch.nn.Linear:
        torch.nn.init.normal_(m.weight,mean=0.,std=0.01)
        torch.nn.init.zeros_(m.bias)

net.apply(init_normal)
# Xavier初始化
def init_xavier(m):
    if type(m)==torch.nn.Linear:
        torch.nn.init.xavier_uniform_(m.weight)

# 自定义层
class CenteredLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self,X):
        return X - X.mean()

layer = CenteredLayer()
print(layer(torch.tensor([1,2,3,4,5],dtype=torch.float32)),layer(torch.tensor([1,2,3,4,5],dtype=torch.float32)).mean())

# 模型保存
# torch.save(net.state_dict(),'./Python/Learning/Deep_Learn/net.pth')
# 模型加载，网络要先定义好
# net.load_state_dict(torch.load('./Python/Learning/Deep_Learn/net.pth'))


X = torch.arange(9.0).reshape(3,3)
print(X.shape)
X = X.reshape((1,1)+X.shape)
print(X.shape)
print(X)



def corr2d(X,K):
    h,w = K.shape
    Y = torch.zeros(X.shape[0]-h+1,X.shape[1]-w+1)
    for i in range(Y.shape[0]):
        for j in range(X.shape[1]):
            Y[i,j] = (X[i:i+h,j:j+w]*K).sum()
    return Y

def corr2d_multi_in(X,K):
    return sum(corr2d(x,k) for x,k in zip(X,K))

def corr2d_multi_in_out(X,K):
    return torch.stack([corr2d_multi_in(X,k) for k in K],0)


X = torch.normal(0,1,(3,3,3))
K = torch.normal(0,1,(2,3,1,1))
Y1 = corr2d_multi_in_out(X,K)
print(Y1.shape)
print(Y1)
print()

def pool2d(X,pool_size,mode='max'):
    p_h,p_w = pool_size
    Y = torch.zeros(X.shape[0]-p_h+1,X.shape[1]-p_w+1)
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode=='max':
                Y[i,j] = X[i:i+p_h,j:j+p_w].max()
            elif mode=='avg':
                Y[i,j] = X[i:i+p_h,j:j+p_w].mean()
    return Y

import torch.nn as nn

def batch_norm(X,gamma,beta,moving_mean,moving_var,eps,momentum):
    if not torch.is_grad_enabled():
        X_hat = (X-moving_mean)/torch.sqrt(moving_var+eps)
    else:
        assert len(X.shape) in (2,4)
        if len(X.shape)==2:
            mean = X.mean(dim=0)
            var = ((X-mean)**2).mean(dim=0)
        else:
            mean = X.mean(dim=(0,2,3),keepdim=True)
            var = ((X-mean)**2).mean(dim=(0,2,3),keepdim=True)
        X_hat = (X-mean)/torch.sqrt(var+eps)
        moving_mean = momentum*moving_mean + (1.0-momentum)*mean
        moving_var = momentum*moving_var + (1.0-momentum)*var
    Y = gamma*X_hat + beta
    return Y,moving_mean,moving_var

lines = ['hello world','hello deep learning']

print([line.split() for line in lines])
print([list(line) for line in lines])

print(isinstance([line.split() for line in lines][0],list))
# print(count_corpus([line.split() for line in lines]))



