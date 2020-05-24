# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
import numpy as np
m1 = np.arange(9).reshape(3,3)
a = np.sin(m1)
m2 = np.arange(1,10).reshape(3,3)
b = np.cos(m2)

print(a+b)