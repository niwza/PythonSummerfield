import string
import sys
import collections


def sort_value(item):
    return item[1]


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1
for word, count in sorted(words.items(), key=sort_value):
    print("'{0}' occurs {1} times".format(word, count))


