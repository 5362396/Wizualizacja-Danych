import numpy as np

x = np.arange(1, 101)
x = x.reshape(10,10)
print(x)
#2
parzysta = [x[i][j] for i in range(0,10) for j in range(0,10) if i %2==0]
nieparzysta = [x[i][j] for i in range(0,10) for j in range(0,10) if i %2==1]
print(parzysta)
print(nieparzysta)
wektor = []
for a in range(0,10):
    for b in range(0,10):
        if a==b:
            wektor.append(x[a][b])
print(wektor)