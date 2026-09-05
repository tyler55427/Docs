import torch
from d2l import torch as d2l
import random

true_w = torch.tensor([2345, -3344.4])
true_b = 234.435

X = torch.normal(0,1,(1000,2))
Y = torch.matmul(X,true_w) + true_b
Y += torch.normal(0,0.01,Y.shape)

w = torch.normal(0,0.01,(2,1),requires_grad=True)
b = torch.zeros(1,requires_grad=True)

batch_size = 10
lr = 0.03
num_epochs = 5



def net(X):
    return torch.matmul(X,w)+b

def loss(y_hat,y):
    return (y_hat-y.reshape(y_hat.shape))**2/2

def sgd(params,lr,batch_size):
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()

def data_iter(batch_size,features,labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0,num_examples,batch_size):
        batch_indices = indices[i:min(i+batch_size,num_examples)]
        yield features[batch_indices], labels[batch_indices]

for epoch in range(num_epochs):
    for X_batch,Y_batch in data_iter(batch_size,X,Y):
        l = loss(net(X_batch),Y_batch)
        l.sum().backward()
        sgd([w,b],lr,batch_size)
    with torch.no_grad():
        train_l = loss(net(X),Y)
        print(f'epoch {epoch+1}, loss {float(train_l.mean()):f}')
        print(f'w: {w}, b: {b}')
