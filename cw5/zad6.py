# Napisz własny iterator, który będzie zwracał tylko elementy z parzystych indeksów przekazanej kolekcji.
class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index == len(self.data):
            raise StopIteration
        if self.index % 2 == 0:
            return self.data[self.index]


napis = Parzyste("pnpnpn")
print(next(napis))
print(next(napis))
print(next(napis))
print(next(napis))
print(next(napis))
print(next(napis))