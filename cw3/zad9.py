#Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów ciągu.
def iloczynciagu(a1=1,r=2,ile=3):
    suma=a1
    a=a1
    for i in range(ile):
        a+=r
        suma*=a
    print(suma)
iloczynciagu(3)