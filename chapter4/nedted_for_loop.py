letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]

result = []
for l in letters:
    print(l)
    for n in numbers:
        print(n)
        result.append(l + str(n))

print(result)
