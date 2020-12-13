c = 340
print(type(c))
print(type('apple'))


def minmax(items):
    print(max(items))
    print('max to' + str(max(items)))
    return min(items), max(items)



minmax([1, 4, 5, 70, -10, 45])
# lower, upper = minimax([1,4,5,70,-10,45])

print(5 in (1, 4, 5, 70, -10, 45))
print(3 in (1, 4, 5, 70, -10, 45))
