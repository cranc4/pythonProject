# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


SIZE = 20

fib = iter(fibonacci())

for _ in range(SIZE):
    print(next(fib))