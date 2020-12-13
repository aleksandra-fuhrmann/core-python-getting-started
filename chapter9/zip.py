prices = [80, 10, 40]
products = ['skirt', 'cup', 'jeans']

for item in zip(prices, products):
    print(item)

l1 = [2, 5, 10, 4, 8, 14, 11, 9]
l2 = [20, 30, 10, 50, 45, 12, 34, 37]

for el1, el2 in zip(l1, l2):
    print('average=', (el1 + el2) / 2)

l3 = [11, 12, 9, 10, 8, 7, 16, 15]


for temps in zip(l1, l2, l3):
    print(temps)
    print(f'min = {min(temps)}, max = {max(temps)}, average= {sum(temps) / 3}')
