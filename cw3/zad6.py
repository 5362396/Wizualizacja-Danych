#Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość promienia. Funkcja ma przyjmować argumenty domyślne: Równanie okręgu dane jest wzorem: (x-a)2+(y-b)2=r2 gdzie (a,b) to środek okręgu a r to promień okręgu.
from math import *
def promien(x,y,a,b):
    return sqrt(pow(x-a,2)+pow(y-b,2))

print(promien(6,4,7,8))