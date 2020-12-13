prices = [30 , 20, 45, 50, 80]
for p in prices:
    print(p)

articels = ['maska', 'fluid', 'krem', 'baza', 'perfum']
for a in articels:
    print(a)

print('joining \n')
if len(prices) == len(articels):
    catalog={}
    for index in range(0,len(prices)):
        print(index)
        price_element=prices[index]
        print(price_element)
        articel_element=articels[index]
        print(articel_element)
        catalog[price_element]=articel_element
        print(catalog)
        print('endofloop')
        print()
    print(catalog)


