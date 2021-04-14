import numpy as np

zera = np.zeros(25)
macierz = zera.reshape((5, 5))
diag = np.diag([1 for x in range(5)])
diag = macierz+diag+np.fliplr(diag)
#zredukowanie środka macierzy do 1 bo wychodzi 2
diag[2][2]=1
print(diag)