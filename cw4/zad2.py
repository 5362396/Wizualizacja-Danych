#Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.
plik=open("podzielne4.txt")
for i in range(100):
    print(plik.readline())
plik.close()