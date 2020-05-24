#Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu arytmetycznego. Funkcja niech przyjmuje jako parametry: a1 (wartość początkowa), r (wielkość o ile rosną kolejne elementy) i ile_elementów (ile elementów ma sumować). Ponadto funkcja niech przyjmuje wartości domyślne: a1= 1, r=1, ile=10.
def sumaciagu(a1=1,r=1,ile=10):
    suma=a1
    a=a1
    for i in range(ile):
        a+=r
        suma+=a
    print(suma)
sumaciagu(2)