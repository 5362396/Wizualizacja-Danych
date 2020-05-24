#Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9
from sys import *
w=int(input("Podaj wysokość diaxa\n"))
for i in range(1,w+1,1):
    for j in range(int((w-1)/2)):
        stdout.write(" ")
    for j in range(i):
        stdout.write("o")
    for j in range(int((w-1)/2)):
        stdout.write(" ")
    stdout.write('\n')