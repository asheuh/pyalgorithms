import pprint
import copy

from itertools import starmap
from time import time
from collections import defaultdict

from read_file import read_data


def parser(line):
    return [i for i in line]

def solve(data):
    def check(a, b):
        match [a, b]:
            case ['.', 'O']:
                return True

            case ['O', '.']:
                return False
            
            case ['O', 'O']:
                return False
            
            case ['.', '#']:
                return True
            case _:
                return False

    scores = defaultdict(int)
    total = 0
    seen = {}

    for i, row in enumerate(data):
        rscore = len(data) - i
        scores[i] = rscore

        for j in range(i):
            indices = [
                (c, boolc) for c, boolc in enumerate(starmap(
                    check,
                    zip(data[j], data[i])
                ))
            ]

            count = 0
            for (k, boolc) in indices:
                if not boolc:
                    if (j, k) not in seen and data[j][k] == 'O':
                        seen[(j, k)] = data[j][k]

                else:
                    x = j
                    is_pound = data[i][k] == '#'
                    if x and data[k-1] == '.' and (x-1, k) not in seen:
                        x -= 1

                    if (x, k) not in seen and not is_pound: 
                        data[i][k], data[x][k] = data[x][k], data[i][k]
                    seen[(x, k)] = data[x][k]

    for i, line in enumerate(data):
        total += sum(1 for c in line if c == 'O') * scores[i]
    return total

if __name__ == '__main__':
    data = read_data('./data/2023/day14_input.txt', parser=parser)
    st = time()
    result = solve(data)
    et = time()
    print('PART ONE ======>', result)
    print('TIME TAKEN ====>', et-st)
