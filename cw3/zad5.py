#Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe: Proste dane równaniami y=a1x+b1, y=a2x+b2, są  równolegle gdy a1=a2 prostopadłe gdy a1a2=-1
def sprawdzenie(y1="2x+b", y2="2x+5b"):
    lista1=y1.split()
    lista2=y2.split()
    if lista1[0][0]==lista2[0][0]:
        print("Funkcje sa rownolegle.")
    elif int(lista1[0][0])*int(lista2[0][0])==-1:
        print("Funkcje sa prostopadle.")
    else :
        print('Funkcje nie sa ani rownolegle ani prostopadle')
sprawdzenie()