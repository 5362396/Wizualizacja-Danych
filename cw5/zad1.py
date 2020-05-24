# Stwórz 3 klasy: Materiał, Ubrania, Swetry. Klasa: Materiał
# Atrybuty:
# •	rodzaj,
# •	długość
# •	szerokość
# Metody:
# •	konstruktor
# •	wyświetl_nazwę
# Klasa: Ubrania
# Atrybuty:
# •	rozmiar
# •	kolor
# •	dla_kogo
# Metody:
# •	wyświetl_dane – do wyświetlania informacji o ubraniu
# klasa: Sweter
# Atrybuty:
# •	rodzaj_swetra – np. Rozpinany, z golfem itd.
# Metody:
# •	wyświetl_dane
# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania. Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.
class Material:
    rodzaj="bawelna"
    dlugosc=0.5
    szerokosc=1.5
    def __init__(self):
        print("Stworzono material.")
    def wyswietlnazwe(self):
        print(self.rodzaj)


class Ubranie(Material):
    kolor="zielony"
    rozmiar="s"
    dla_kogo="dla klienta"
    def __init__(self):
        print("Stworzono ubranie.")
    def wyswietldane(self):
        print(self.kolor,self.rozmiar,self.dla_kogo)


class Sweter(Ubranie):
    rodzaj_swetra="Golf"
    def __init__(self):
        print("Stworzono sweter.")
    def wyswietinfo(self):
        print(self.rodzaj_swetra)

material=Material()
ubranie=Ubranie()
sweter=Sweter()