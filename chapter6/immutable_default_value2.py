def clearing_list(menu=None):
    if menu is None:
        return ['spam']
    elif 'spam' not in menu:
        menu.append('spam')
        return menu

l=['ważne','reklamy']
print(clearing_list(l))
print(clearing_list(l))





