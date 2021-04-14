import matplotlib.pyplot as mpl
import numpy as np

lista1 = [pow(x,2)*np.pi for x in range(-10,11)]
lista2 = [x for x in range(-10,11)]
mpl.plot(lista2, lista1, label='funkcja')
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.legend()

mpl.show()