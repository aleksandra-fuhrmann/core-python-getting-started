def add_spam(menu=None):#list clearing to keep it empty
    if menu is None:
        menu=[]
    menu.append('spam')
    return menu

print(add_spam())
print(add_spam())
print(add_spam())

l=['wazne','reklamy']
print(add_spam(l))
print(add_spam(l))# tu w ifie nie jest None wiec po prostu przechodzi od razu do manu.append('spam') i modyfikuje liste, nie usuwajac poprzednio dodanych spam




