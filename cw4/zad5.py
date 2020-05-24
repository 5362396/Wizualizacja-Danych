#Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
#•	wyświetl_dane – drukuje elementy na ekran
#•	pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
#•	pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
#•	policz_sume – liczy sume elementow
#•	policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
#Stwórz instancję klasy i sprawdź działanie wszystkich metod.
class Ciag:
    a=1
    r=5
    n=3
    def __init__(self,a=1,r=5,n=3):
        self.a=a
        self.r=r
        self.n=n
    def pobierzelementy(self):
        print("nie ma")
        #tutaj jakies wygibasy beda

    def pobierzparametry(self,a,r):
        self.a=a
        self.r=r
    def policzsume(self):
        suma=0
        element=self.a
        for i in range(self.n):
            suma+=element
            element+=self.r
        print(suma)
    def policzelementy(self):
        element=self.a
        for i in range(self.n):
            print(i,"", element)
            element+=self.r

test=Ciag(0,2,8)
test.policzsume()
test.policzelementy()