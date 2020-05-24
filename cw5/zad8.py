# Przepisz jeden z napisanych przez siebie iteratorów na generator.
def gen(data):
    for i in range(len(data)):
        if i % 2 == 0:
            yield data[i]


tekst = gen("Dlugi tekst bardzo")
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))
print(next(tekst))