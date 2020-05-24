#Napisz skrypt, w którym użytkownik ma podać liczbę i który będzie wyłapywał błąd gdy użytkownik poda literę zamiast cyfry.
try:
    l=int(input("Podaj liczbę\n"))
    liczby=[1,2,3,4,5,6,7,8,9,0]
    for i in liczby:
        if(l==liczby[i]):
            print("To liczba którą podałeś:", liczby[i])
except ValueError:
    print("Nie podałeś liczby")