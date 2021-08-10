import torch
a = torch.rand(2, 4)
b = a.view(8)
c = b.view(4, 2)
const = torch.ones_like(c)
print('a ', a)
print('b ', b)
print('c ', c)
c.add_(const)
print('inplace update view tensor c also updates its aliases')
print('a ', a)
print('b ', b)
print('c ', c)