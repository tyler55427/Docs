# 概率
import torch
from torch.distributions import multinomial

fair_=torch.ones([6])/6
print(multinomial.Multinomial(100000,fair_).sample())

