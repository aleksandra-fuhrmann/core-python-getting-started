library = {'A': 1, 'B': 2}

try:
    print(library['B'])
except KeyError:
    print("No such key")
