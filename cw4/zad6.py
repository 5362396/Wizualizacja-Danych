# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
# •	sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
# •	sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
# •	sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# •	wyświetl_wyrazy – wyświetla podane wyrazy
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.
class Slowa:
    slowo1="arka"
    slowo2="gdynia"
    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def czypalindrom(self):
        isit=True
        for i in range(int(len(self.slowo1)/2)):
            if(self.slowo1[i]!=self.slowo1[len(self.slowo1)-1-i]):
                isit=False
        if isit==False:
            print("nie jest")
        else:
            print("jest")
    def czymetagramy(self):
        print("do zrobienia")
    def czyanagramy(self):
        print("do zrobienia")
    def wyswietlwyrazy(self):
        print(self.slowo1)
        print(self.slowo2)
test=Slowa("kamilslimak","oho")
test.wyswietlwyrazy()
test.czypalindrom()