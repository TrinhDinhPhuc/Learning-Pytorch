import numpy as np
import torch
a = np.random.rand(4,3)
print(type(a))
print(a)

b = torch.from_numpy(a)
print(type(b))
print(b)

#Tensor - > numpy
print(b.numpy())

print(b.mul_(2))