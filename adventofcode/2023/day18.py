import pprint

from collections import defaultdict

from read_file import read_data


def directions(d, prev, r):
    x, y = prev
    match d:
        case 'R':
            return (x, r + y)
        
        case 'L':
            return (x, (-1 * r) + y)

        case 'U':
            return (x + (-1 * r), y)

        case 'D':
            return (r + x, y)

        case _:
            return (x, y + r)

def pparser(line):
    mapper = {
        0: 'R',
        1: 'D',
        2: 'L',
        3: 'U'
    }
    line = tuple(line.split(' '))
    _, _, hexcode = line
    dd = hexcode[-2:-1]
    steps = int(f'0x{hexcode[2:-2]}', 16)
    d = mapper[int(dd)]
    return d, steps, hexcode

def parser(line):
    return tuple(line.split(' '))

def turns(dplan):
    prev = (0, 0)
    bcubes = {prev: True}

    for plan in dplan:
        d, c, ccode = plan
        assert int(c)

        c = int(c)
        x, y = directions(d, prev, c)
        prev = (x, y)
        bcubes[prev] = True
    return list(bcubes.keys()) 

def total_polygon_len(turns):
    total = 0
    l = len(turns)
    for i, (x, y) in enumerate(turns):
        ni = (i + 1) % l
        total += abs(turns[ni][0] - x) + abs(turns[ni][1] - y)
    return total

def digger(dplan):
    all_turns = turns(dplan)
    total = total_polygon_len(all_turns)
    return digenclosed(total, all_turns)

def digenclosed(t, points):
    # finding the area of the polygon using shoelace formula
    # https://en.wikipedia.org/wiki/Shoelace_formula
    # The calculating the number of points inside the polygon using Pick's theorem
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    points = points + [points[0]] 
    n = len(points)
    pair_points = []
    i, j = 0, 1

    while j < n:
        pair = (points[i], points[j])
        pair_points.append(pair)
        i += 1
        j += 1

    area = 0
    for pair in pair_points:
        (a, b), (c, d) = pair
        dt = (a * d) - (c * b)
        area += dt

    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    count = (area // 2) - t // 2 - 1
    return abs(count)

def is_point_in_path(x, y, poly):
    # https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
    n = len(poly)
    j = n - 1
    is_inside = False
    for i in range(n):
        if (x == poly[i][0]) and (y == poly[i][1]):
            return True

        if (poly[i][1] > y) !=  (poly[j][1] > y):
            slope = (x - poly[i][0]) * (
                poly[j][1] - poly[i][1]
            ) - (poly[j][0] - poly[i][0]) * (y - poly[i][1])

            if slope == 0:
                return True

            if (slope < 0) != (poly[j][1] < poly[i][1]):
                is_inside = not is_inside
        j = i
    return is_inside

def solve_part_one(dplan):
    return digger(dplan) 

def solve_part_two(dplan):
    return digger(dplan)

def get_data(mparser):
    return read_data('./data/2023/day18_input.txt', parser=mparser)


if __name__ == '__main__':
    dplan = get_data(parser) 
    result = solve_part_one(dplan)
    print('PART ONE', result)

    dplan = get_data(pparser) 
    pt_result = solve_part_two(dplan)
    print('PART TWO', pt_result)
