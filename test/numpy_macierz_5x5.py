import numpy as np
import matplotlib.pyplot as plt

macierz = np.arange(1, 26)
macierz = macierz.reshape((5, 5))

for i in range(0, 5):
    macierz[i, i] = 0

print(macierz)