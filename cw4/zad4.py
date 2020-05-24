#Stwórz klasę NaZakupy, która będzie przechowywać  atrybuty: nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
#•	konstruktor – który nadaje wartości
#•	wyświetl_produkt() – drukuje informacje o produkcie na ekranie
#•	ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
#•	Ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2
class NaZakupy:
    nazwa_produktu="jajka"
    ilosc=12
    jed_miary="ilosc"
    cena=0.4
    def __init__(self,nazwa_produktu,ilosc,jed_miary,cena):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jed_miary=jed_miary
        self.cena=cena
    def wyswietl_produkt(self):
        print("nazwa",self.nazwa_produktu)
        print("ilosc",self.ilosc)
        print("jednostka",self.jed_miary)
        print("cena za jednostke",self.cena)
    def ile_produktu(self):
        print(self.nazwa_produktu,self.ilosc)
    def ile_kosztuje(self):
        print(self.cena*self.ilosc)
jajka=NaZakupy("jajka",10,"ilosc",0.4)
print(jajka)
jajka.wyswietl_produkt()
jajka.ile_produktu()
jajka.ile_kosztuje()