from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')

story_words = []
for line in story:
    line_words = line.split()
    print(line_words)
    for word in line_words:
        print(word)
        story_words.append(word)
print(story_words)


story = urlopen('http://sixty-north.com/c/t.txt')

story_words = []
for line in story:
    line_words = line.split()
    story_words= story_words+line_words
print(story_words)


