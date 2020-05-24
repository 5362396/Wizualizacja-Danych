#Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
with open("zad3.txt",'w') as plik:
    plik.write("wpisywanko\n")
    plik.write("tekstu\n")
    plik.write("do\n")
    plik.write("pliku\n")
with open("zad3.txt",'r') as plik:
    odczyt=plik.readline()
    while odczyt:
        print(odczyt)
        odczyt=plik.readline()