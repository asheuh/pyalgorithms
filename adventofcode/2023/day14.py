import pprint
import copy

from itertools import starmap
from time import time
from collections import defaultdict, Counter

from read_file import read_data


def parser(line):
    return [i for i in line]

def transpose(grid):
    return list(list(c) for c in zip(*grid))

def check_direction(direction):
    match direction:
        case 'N':
            return 0, 1, lambda x, y: x < y

        case 'W':
            return 0, 1, lambda x, y: x < y

        case 'S':
            return 1, -1, lambda x, y: x >= y

        case 'E':
            return 1, -1, lambda x, y: x >= y

        case _:
            return 0, 1, lambda x, y: x < y

def slow_solve(data):
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
    f = transpose(data)
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

def fast_solve(grid, func=lambda a: a, direction='N'):
    scores = {i: (len(grid) - i, []) for i, _ in enumerate(grid)}
    f = func(grid)

    for i, row in enumerate(f):
        n = len(row)
        m, sign, g = check_direction(direction)
        counter = Counter(row)
        o = counter['O']
        k = n * m

        while g(k, n):
            c = row[k]
            if c == 'O':
                if o != 0:
                    scores[k][1].append(1)
                    o -= 1
                else:
                    row[k] = '.' # we have used this O

            if c == '.' and o != 0:
                x = k + sign
                t = 0
                while g(x, n):
                    h = row[x]
                    if h != '#':
                        if h == 'O':
                            t += 1
                            break
                    else:
                        break
                    x += sign

                if t > 0:
                    scores[k][1].append(1)
                    row[k] = 'O'
                    row[x] = '.'
                    o -= 1

            if c == '#' or c == '.':
                if o <= 0:
                    break
            k += sign
        f[i] = row
    return sum(s * sum(l) for key, (s, l) in scores.items())

if __name__ == '__main__':
    data = read_data('./data/2023/day14_input.txt', parser=parser)
    st = time()
    result = slow_solve(data)
    et = time()
    print('PART ONE SLOW ======>', result)
    print('TIME TAKEN SLOW ====>', et-st)
    print()
    st = time()
    result = fast_solve(data, transpose)
    et = time()
    print('PART ONE FAST ======>', result)
    print('TIME TAKEN FAST ====>', et-st)
