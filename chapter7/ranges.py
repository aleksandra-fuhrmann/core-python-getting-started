l = [4, 67, 8, 9, 11]
for i in l:
    print(i)

for i in enumerate(l):
    print(i)

for numero,i in enumerate(l,100):
    print(numero, i)

for i,v in enumerate(l):
    print(f'i={i}, v={v}')
    #print('i={i}, v={v}')



