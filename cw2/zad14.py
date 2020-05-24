#Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd
from math import *
l=float(input("Podaj liczbę do wsadzenia pod pierwiastek\n"))
if l<0:
    print("Nie da się zrobić pierwiastka z liczby ujemnej")
else:
    print(sqrt(l))