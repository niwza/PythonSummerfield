import random
import sys

rows = 5
try:
    if sys.argv[1]:
        num = int(sys.argv[1])
        if 1 <= num <= 10:
            rows = num
except (IndexError, ValueError):
    pass
# except ValueError:
#     print("Usage: ", sys.argv[0], " <int>")
#     sys.exit(1)

articles = ["the", "a"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]

row = 0
while row < rows:
    if random.randint(0, 1):
        print(random.choice(articles), random.choice(subjects), random.choice(verbs),
              random.choice(adverbs))
    else:
        print(random.choice(articles), random.choice(subjects), random.choice(verbs))
    row += 1
