exclude_list = ['reklamy', 'spam']


def clearing_list(menu=None):
    clear_list = []
    if menu is not None:
        for item in menu:
            if item not in exclude_list:
                clear_list.append(item)

    return clear_list


l = ['ważne', 'reklamy', 'spam', 'not_spam']
print(clearing_list(l))
print(clearing_list())
print(clearing_list([]))
