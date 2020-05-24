#Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej: y = a x + b Funkcja jest rosną ca gdy a>0 malejąca jeżeli a<0 stała gdy a=0 i w zależności od tego będzie wyświetlać odpowiedni komunikat
def monotonicznosc(y="-3x+2"):
    lista=y.split()
    print(lista)
    if(lista[0][0]=="-"):
        print("Funkcja jest malejaca.")
    else:
        if(int(lista[0][0])>0):
            print("Funkcja jest rosnaca.")
        if(int(lista[0][0])==0):
            print("Funkcja jest stala.")
monotonicznosc()
monotonicznosc(y="5x-3")
monotonicznosc(y="0x+3")