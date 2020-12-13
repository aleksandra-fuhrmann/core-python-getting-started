def square(x):
    return x * x


square(5)
print(square(5))


def ending(value):
    s = str(value)
    if s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    elif s.endswith('11'):
        return 'th'
    return 'th'

def numberw(value):
    return str(value) + ending(value)


print(numberw(3))

def fetch_words():
  story = urlopen('http://sixty-north.com/c/t.txt')
  story_words = []
  for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
    story.close()

    for word in story_words:
        print(word)




