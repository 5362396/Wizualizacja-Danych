import numpy as np

a = np.arange(1,21)
a = a.reshape((5,4))
np.random.shuffle(a)
print(a)
print(a.sum(axis=1))
a = a.astype('float64')
print(a)

for i in range(0,5):
    for j in range(0,4):
        a[i,j]=pow(a[i,j],1/2)
print(a)
a = a.flatten()
a = np.sort(a)
print(a)