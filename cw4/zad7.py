# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
# •	konstruktor – który nadaje wartość dla x, y i krok
# •	idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
# Stwórz instancję klasy i sprawdź jak działają wszystkie metody
class Robaczek:
    x=0
    y=0
    krok=1
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ilosckrokow):
        self.y+=(ilosckrokow*self.krok)
    def idz_w_dol(self,ilosckrokow):
        self.y-=(ilosckrokow*self.krok)
    def idz_w_lewo(self,ilosckrokow):
        self.x-=(ilosckrokow*self.krok)
    def idz_w_prawo(self,ilosckrokow):
        self.x+=(ilosckrokow*self.krok)
    def pokaz_gdzie_jestes(self):
        print(self.x," ",self.y)
    def __del__(self):
        print("Robaczek zginął")
robak=Robaczek(1,1,1)
robak.pokaz_gdzie_jestes()
robak.idz_w_dol(1)
robak.pokaz_gdzie_jestes()