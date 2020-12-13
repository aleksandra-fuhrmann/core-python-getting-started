from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def printingOfList(s):
    for line in s:
        print(line)


if __name__ == '__main__':
    printingOfList(fetch_words())

# def sum(a, b):
# return a + b


# if __name__ == '__main__':
# printingOfList([1,3,5])
# printingOfList([2,5])
