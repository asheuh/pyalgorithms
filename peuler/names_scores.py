import pprint
import string


def name_score(names):
    alphabets = string.ascii_uppercase
    alphamap = {c: i + 1 for i, c in enumerate(alphabets)}
    total = 0

    for index, item in enumerate(names):
        name = item[1:-1] # ignore first and last quote: ""
        alphavalue = 0
        pos = index + 1

        for i in range(len(name)):
            alphavalue += alphamap[name[i]]
        score = alphavalue * pos # The score of this name
        total += score
    return total


if __name__ == '__main__':
    names = open('names.txt').read().rstrip().split(',')
    names.sort()
    res = name_score(names)
    print(res)
