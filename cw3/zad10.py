#Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów  w postaci: klucz to nazwa produktu  a wartość to ilość. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać tę wartość.
def lista(** rzeczy):
    ilosc=0
    for cos in rzeczy:
        print(cos,"x",rzeczy[cos])
        ilosc+=int(rzeczy[cos])
    return ilosc
a=lista(jablko=4,banan=3,mandarynka=2)
print(a)