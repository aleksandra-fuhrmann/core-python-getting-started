def square():
    i = 1
    while True:
        yield i * i
        i = i + 1  # i+=i


for number in square():
    if number > 100:
        break
    print(number)


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


for x in lucas():
    print(x)
