#Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.
a="abc"
b=1.1
c=hex(40)
print('%(string)s %(float)f %(hex)s' %{'string':a,'float':b,'hex':c})