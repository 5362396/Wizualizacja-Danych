# Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.
def gen():
    x = 0
    y = 1
    for i in range(100):
        z = x + y
        yield z
        x = y
        y = z

fib = gen()
for i in range(10):
    print(next(fib))