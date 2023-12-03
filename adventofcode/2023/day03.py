from functools import reduce

from read_file import read_data


from python.pyalgorithms.utils import *


def get_num(grid, cord, inc):
    num = ""
    h = len(grid)
    w = len(grid[0])
    r, k = cord
    seen = set()
    while True:
        v = Vector(r, k, h, w)
        if not v.is_inside() or not grid[r][k].isdigit():
            break
        
        _chr = grid[r][k]
        num += _chr
        seen.add((r, k))
        k -= inc
    return num, seen

def solve(grid, isparttwo=False):
    done = set() 
    parts = []
    mapp = create_map(grid)
    total_gratio = 0 # total gear ratio

    for coord, char_neighbours in mapp.items():
        r, c = coord
        char, neighbours = char_neighbours
        star_values = []

        for neighb in neighbours:
            nr, nc = neighb.x, neighb.y 
            nchar = grid[nr][nc]
            if not nchar.isdigit() or (nr, nc) in done:
                continue

            # found part number
            backpnumber, bseen = get_num(grid, (nr, nc-1), 1)
            frontpnumber, fseen = get_num(grid, (nr, nc+1), -1)
            done |= (bseen | fseen)
            partn = ''.join(reversed(backpnumber)) + nchar + frontpnumber
            y = int(partn)
            parts.append(y)

            if isparttwo and char == '*':
                # check if is gear
                star_values.append(y)

        if len(star_values) == 2:
            # Found gear
            total_gratio += reduce(lambda x, y: x * y, star_values)
        done.add(coord)

    if isparttwo:
        return total_gratio
    return sum(parts)

def create_map(grid):
    mapp = {}
    h = len(grid) # height
    w = len(grid[0]) # width

    for x, row in enumerate(grid):
        for y, point in enumerate(row):
            if not point.isdigit() and not point.isalpha() and point != '.':
                vecs = neighbouring_vectors((x, y), h, w, 'all')
                mapp[(x, y)] = (point, vecs)
    return mapp


if __name__ == '__main__':
    data = read_data('../data/2023/day03_input.txt')
    result = solve(data)
    print("PART ONE: ", result)
    ptresult = solve(data, True)
    print("PART TWO: ", ptresult)
