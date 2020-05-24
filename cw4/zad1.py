#Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
plik=open("podzielne4.txt",'w')
for i in range(100):
    p=i*4
    plik.write(str(p))
    plik.write('\n')
plik.close()