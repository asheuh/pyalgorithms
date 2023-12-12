import pprint

from time import time
from collections import defaultdict
from itertools import combinations

from read_file import read_data


def solve(data, rate):
    universes = universe_cordinates(data)
    universes, pairs = expand_universe(universes, data, rate)
    total = 0

    for pair in pairs:
        (x, y), (r, c) = pair
        total += abs(r-x) + abs(c-y)
    return total

def universe_cordinates(universes):
    nuniverses = []
    for i in range(len(universes)):
        line = []
        for j in range(len(universes[0])):
            line.append((universes[i][j], (i, j)))
        nuniverses.append(line)
    return nuniverses

def expand_universe(universes, data, rate):
    def expand_cols(universes, rate, is_expand=True):
        expanded_universe = []
        r = 0
        for i, ss in enumerate(universes[0]):
            line = []
            for j, row in enumerate(universes):
                line.append(universes[j][i])

            if is_expand and '#' not in [v for v, _ in line]:
                expanded_universe.append([(v, (x, y + r)) for v, (x, y) in line])
                r += (rate - 1)
                continue

            expanded_universe.append([(v, (x, y + r)) for v, (x, y) in line])
        return expanded_universe

    def expand_rows(universes, rate):
        nuni = []
        r = 0
        for line in universes:
            if '#' not in [v for v, _ in line]:
                nuni.append([(v, (x + r, y)) for v, (x, y) in line])
                r += (rate - 1)
                continue

            nuni.append([(v, (x + r, y)) for v, (x, y) in line])
        return nuni

    nu = expand_rows(universes, rate)
    expandone = expand_cols(nu, rate)
    expandtwo = expand_cols(expandone, rate, False)
    pairs = get_pairs(expandtwo)
    return expandtwo, pairs

def get_pairs(universes):
    cords = []
    for i, row in enumerate(universes):
        for j, point in enumerate(row):
            v, (x, y) = point
            if v == '#':
                cords.append((x, y))
    return combinations(cords, 2)

if __name__ == '__main__':
    data = read_data('./data/2023/day11_input.txt')
    st = time()
    result = solve(data, 2)
    pt_result = solve(data, 1000000)
    et = time()
    print('PART ONE =>', result)
    print('PART TWO =>', pt_result)
    print('TIME TAKEN =>', et - st)
