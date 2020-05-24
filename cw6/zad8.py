# Napisz funkcję, która:
# - jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# - parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# - funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)
import numpy as np

def pol(tab, kierunek):
    z = tab.shape
    x = z[0]
    y = z[1]

    if kierunek == 0 and x % 2 != 0:
        print("Nie moge tego zrobic")
        return -1
    if kierunek == 1 and y % 2 != 0:
        print("Nie moge tego zrobic")
        return -1
    if kierunek == 0:
        a = tab[:int(x / 2)]
        b = tab[int(x / 2):int(x)]
    if kierunek == 1:
        a = tab[:, :int(y / 2)]
        b = tab[:, int(y / 2):int(y)]
    print(a)
    print(b)

tab1 = np.array([[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9], [9, 10, 11, 12]])
print(tab1)
pol(tab1, 1)