from urllib.request import urlopen


def sum(a, b):
    return a + b


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


print(__name__)
if __name__ == '__main__':
    # fetch_words()
    print(fetch_words())
    # print(sum(1,3))
    s = sum(1, 3)
    print()
