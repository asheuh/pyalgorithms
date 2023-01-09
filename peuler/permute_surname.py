import pprint

from time import sleep
from itertools import permutations


if __name__ == '__main__':
    generater = permutations('scamkanoa')
    for g in generater:
        name = ''.join(g)
        print(name)
