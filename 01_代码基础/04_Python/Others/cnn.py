import torch
from torch import nn
import math

class Temp(nn.Module):
    def __init__(self):
        super(Temp, self).__init__()
        self.w1 = nn.Parameter(torch.tensor([[1.0, 0.7],
                                             [-1.0, 0.3],
                                             [0.5, -0.8]], requires_grad=True))
        self.w2 = nn.Parameter(torch.tensor([[1.2], [-1.5]], requires_grad=True))
        
    def forward(self, x):
        # 保存 sigmoid 激活前的中间值
        self.z1 = torch.matmul(x, self.w1)  # 激活前的输入
        self.z1.retain_grad()  # 保留 z1 的梯度
        print("z1 (before sigmoid):", self.z1)
        x = torch.sigmoid(self.z1)
        self.sigmoid_z1 = x  # 保存 sigmoid(z1) 的值
        self.sigmoid_z1.retain_grad()  # 保留 sigmoid(z1) 的梯度
        print("sigmoid(z1):", x)
        
        self.z2 = torch.matmul(x, self.w2)  # 激活前的输入
        self.z2.retain_grad()  # 保留 z2 的梯度
        print("z2 (before sigmoid):", self.z2)
        x = torch.sigmoid(self.z2)
        self.sigmoid_z2 = x  # 保存 sigmoid(z2) 的值
        self.sigmoid_z2.retain_grad()  # 保留 sigmoid(z2) 的梯度
        print("sigmoid(z2):", x)
        
        return x
    
if __name__ == "__main__":
    model = Temp()
    x = torch.tensor([[1.0, 0.0, 1.0]], requires_grad=True)
    y = torch.tensor([[1.0]])
    loss_fn = nn.BCELoss()  # 使用二分类交叉熵损失，因为输出是 sigmoid
    y_pred = model(x)
    loss_value = loss_fn(y_pred, y)
    print("Loss value:", loss_value.item(), -math.log(y_pred))
    
    # 反向传播
    loss_value.backward()
    
    # 打印每个参数的梯度
    print("Gradients for w1:", model.w1.grad)
    print("Gradients for w2:", model.w2.grad)
    
    # 打印输入 x 的梯度
    print("Gradients for input x:", x.grad)
    
    # 打印 sigmoid 激活后的梯度
    print("Gradients for sigmoid(z1):", model.sigmoid_z1.grad)
    print("Gradients for sigmoid(z2):", model.sigmoid_z2.grad)
