#Zdefiniuj następujące zbiory, wykorzystując Python comprehension: A={1/x:  xc<1,10>} B={1, 2, 4, 8,…, 2^10} C={x: xcB i x jest liczbą podzielną przez 4}
from math import *
zbior=[(1/i) for i in range(1,11,1)]
print(zbior)
zbior2=[(pow(2,i))for i in range(10)]
print(zbior2)
zbior3=[(i)for i in range(0,10,4)]
print(zbior3)