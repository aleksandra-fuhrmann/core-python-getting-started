x = range(3, 6)
for n in x:
    print(n)

from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

for x in range(10):
    print(x, is_prime(x))

# print([x for x in range(10) if jest_pierwsza(x)])

