import torch
from d2l import torch as d2l
x=torch.arange(20).reshape((1,1,4,5))
y=torch.arange(4).reshape((1,1,2,2))
z=torch.conv2d(x,y)
print(z)