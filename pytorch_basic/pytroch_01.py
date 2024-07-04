import torch
import numpy as np

n1 = np.arange(10).reshape(2,5)
n2 = np.arange(10).reshape(5,2)
t1 = torch.FloatTensor(n1)
t2 = torch.FloatTensor(n2)

print("t1 = ", t1)
print("t2 = ", t2)

print(t1.mm(t2))