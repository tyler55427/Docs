import torch
from d2l import torch as d2l
import math
from torch import nn
from torch.nn import functional as F


# tokens=d2l.tokenize(d2l.read_time_machine())
# corpus=[token for line in tokens for token in line]
# vocab=d2l.Vocab(corpus)

batch_size, num_steps = 32, 35
train_iter, vocab = d2l.load_data_time_machine(batch_size, num_steps)

num_epochs, lr = 500, 1
device = d2l.try_gpu()
loss = nn.CrossEntropyLoss()
gru_layer = nn.GRU(input_size=len(vocab), hidden_size=256)
model = d2l.RNNModel(gru_layer, len(vocab))
d2l.train_ch8(model, train_iter, vocab, lr, num_epochs, device)

