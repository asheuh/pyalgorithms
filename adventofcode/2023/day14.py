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

def check_direction(direction, n=None):
    match direction:
        case 'N':
            return 0, 1, lambda x, y: x < y, n, transpose

        case 'W':
            return 0, 1, lambda x, y: x < y, n, lambda a: a

        case 'S':
            return 1, -1, lambda x, y: x >= y, 0, transpose 

        case 'E':
            return 1, -1, lambda x, y: x >= y, 0, lambda a: a 

        case _:
            return 0, 1, lambda x, y: x < y, n, transpose

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

def tilt(grid, func=lambda a: a, direction='N'):
    scores = {i: (len(grid) - i, []) for i, _ in enumerate(grid)}
    f = func(grid)

    for i, row in enumerate(f):
        n = len(row)
        m, sign, g, j, _ = check_direction(direction, n)
        counter = Counter(row)
        o = counter['O']
        k = (n * m) + (sign * m)

        while g(k, j):
            y = k if direction in ['N', 'S'] else i
            c = row[k]
            if c == 'O':
                if o != 0:
                    scores[y][1].append(1)
                    o -= 1
                else:
                    row[k] = '.' # we have used this O

            if c == '.' and o != 0:
                x = k + sign
                t = 0
                while g(x, j):
                    h = row[x]
                    if h != '#':
                        if h == 'O':
                            t += 1
                            break
                    else:
                        break
                    x += sign

                if t > 0:
                    scores[y][1].append(1)
                    row[k] = 'O'
                    row[x] = '.'
                    o -= 1

            if c == '#' or c == '.':
                if o <= 0:
                    break
            k += sign
        f[i] = row
    return sum(s * sum(l) for key, (s, l) in scores.items()), func(f)

def solve_part_one(grid):
    return tilt(grid, transpose)

def solve_part_two(grid, cycles):
    directions = ['N', 'W', 'S', 'E']
    history = [(0, grid)]
    out = 0
    
    for i in range(cycles):
        for direction in directions:
            _, _, _, _, func = check_direction(direction)
            out, grid = tilt(grid, func, direction)
        
        if (out, grid) in history:
            k = history.index((out, grid))
            c = (i + 1) - k
            f = (cycles - k) % c + k
            o, hist = history[f]
            return o
        history.append((out, grid))
    return out 

if __name__ == '__main__':
    data = read_data('./data/2023/day14_input.txt', parser=parser)
    st = time()
    result = slow_solve(data)
    et = time()
    print('PART ONE SLOW ======>', result)
    print('TIME TAKEN SLOW ====>', et-st)
    print()
    st = time()
    result, _ = solve_part_one(data)
    et = time()
    print('PART ONE FAST ======>', result)
    print('TIME TAKEN FAST ====>', et-st)
    print()

    st = time()
    cycles = 1_000_000_000
    result = solve_part_two(data, cycles)
    et = time()
    print('PART TWO ======>', result)
    print('TIME TAKEN ====>', et-st)
