import random


def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames,"data/forenames.txt"),
                            (surnames, "data/surnames.txt")):
        for name in open(filename, encoding="utf8"):
            names.append(name.rstrip())
    return forenames, surnames


forenames, surnames = get_forenames_and_surnames()
limit = 100
years = list(range(1970, 2013)) * 3
fh = open("test-names1.txt", "w", encoding="utf8")
for year, forename, surname in zip(
        random.sample(years, limit),
        random.sample(forenames, limit),
        random.sample(surnames, limit)):
    name = "{0} {1}".format(forename, surname)
    fh.write("{0:.<25}.{1}\n".format(name, year))
