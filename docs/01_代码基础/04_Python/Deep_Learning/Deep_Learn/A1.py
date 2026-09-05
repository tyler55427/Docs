import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

x=torch.arange(12)
print(x)
print(x.shape)
print(x.numel())
x=x.reshape(3,4)
# 自动计算
# x.reshape(-1,3)

torch.zeros((2,3,4))
torch.ones((2,3,4))

# 正态分布
torch.randn(3,4)

# 张量连结
y=torch.arange(12).reshape(3,4)
print(torch.cat((x,y),dim=0)) # dim是张量轴
print(torch.cat((x,y),dim=1))

print(x==y)

print(x.sum())

# 广播机制
print('广播机制')
a=torch.arange(3).reshape(3,1)
b=torch.arange(2).reshape(1,2)
print(a+b)


print(x[-1])
# 左开右闭？
print(x[1:3])
x[1,2]=9

# 内存节省
# 使用切片
# x=x+y 会使用新的一片内存，而x+=y和x[:]=x+y不会



# 数据处理
# 插值法 和 删值法
# 使用pandas模块


# 降维
x=torch.arange(12)
x=x.reshape((3,4))
print(x.sum([0])) # 将每列的元素求和
print(x.sum(axis=1)) # 将每行的元素求和

# 非降维求和
print(x.sum(axis=1,keepdim=True))
print(x.cumsum(axis=0))

# 点积
x=torch.arange(4)
y=torch.arange(4)
print(torch.dot(x,y))
print(torch.sum(x*y))

# 向量积
x=torch.arange(40).reshape(8,5)
y=torch.arange(5)
print(torch.mv(x,y))

# 矩阵乘法
x=torch.arange(20,dtype=torch.float32).reshape(4,5)
y=torch.ones(40).reshape(5,8)
print(torch.mm(x,y))




# 范数
u=torch.tensor([-3.0,4.0])
print(torch.norm(u)) # 二维范数
print(torch.abs(u).sum()) # 一维范数
print()



# 梯度
# 梯度和x有相同的形状，如果函数是直接由向量x构成的，可以直接求导得到梯度
x=torch.arange(4.0)
x.requires_grad_(True)
y=2*torch.dot(x,x)
y.backward() # 反向传播函数，自动计算梯度
print(x.grad) # 储存梯度
print(x.grad == 4*x)
# 默认pytorch的梯度会累积，要清除
x.grad.zero_()
y=x.sum()
y.backward()
print(x.grad)
print()

# 对于y不是标量的的梯度是一个高阶张量
x.grad.zero_()
y=x*x
y.sum().backward() # 这里没有计算微分矩阵，只是计算偏导数之和
print(x.grad)




# 分离计算
x.grad.zero_()
y=x*x
u=y.detach()
z=u*x
z.sum().backward()
print(x.grad)


a=torch.randn(size=(),requires_grad=True)
def f(a):
    b=2*a
    while b.norm()<1000:
        b=b*2;
    if b.sum()>0:
        c=b
    else:
        c=100*b
    return c
d=f(a)
d.backward()
print(a.grad==d/a)