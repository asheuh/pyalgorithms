import pprint

from read_file import read_data
from python.pyalgorithms.utils import Vector


def next_direction(where, cord, char, hw): 
    match char:
        case '|':
            to = {
                (0, 1): [(1, 0), (-1, 0)], # from left to down and up
                (0, -1): [(1, 0), (-1, 0)], # from right to down and up
                (1, 0): [(1, 0)], # from up for down
                (-1, 0): [(-1, 0)]  # from down to up
            }[where]
            return plus(to, cord, hw)

        case '-':
            to = {
                (1, 0): [(0, 1), (0, -1)], # from up to left and right
                (-1, 0): [(0, 1), (0, -1)], # from down to left and right
                (0, 1): [(0, 1)], # from left, go left
                (0, -1): [(0, -1)] # from right, goright 
            }[where]
            return plus(to, cord, hw)

        case '\\':
            to = {
                (0, 1): [(1, 0)], # from left go down
                (0, -1): [(-1, 0)], # from right go up
                (1, 0): [(0, 1)], # from up go right
                (-1, 0): [(0, -1)] # from down, go left
            }[where]
            return plus(to, cord, hw)

        case '/':
            to = {
                (0, 1): [(-1, 0)], # from left, go up
                (0, -1): [(1, 0)], # from right, go down
                (1, 0): [(0, -1)], # from up, go left
                (-1, 0): [(0, 1)]  # from down, go right
            }[where]
            return plus(to, cord, hw)

        case '.':
            to = {
                (0, 1): [(0, 1)], # from left, keep going right
                (0, -1): [(0, -1)], # from right, keep going left
                (1, 0): [(1, 0)], # from up, keep going down
                (-1, 0): [(-1, 0)] # from down, keep going up
            }[where]
            return plus(to, cord, hw)

        case _:
            return [cord]

def plus(to_add, cord, hw):
    h, w = hw
    cords = []
    for (r, c) in to_add:
        _, (x, y)  = cord
        v = Vector(x, y, h, w)
        nv = v.plus(v, r, c)
        if nv.is_inside():
            cords.append(((r, c), (nv.x, nv.y)))
    return cords

def contains(iterable, item):
    return item in iterable

def move_beam(grid, where, start):
    mapper = [[0] * len(grid[0]) for _ in grid]
    hw = (len(grid), len(grid[0]))
    queue = [(where, start)]
    seen = {start}
    count = 0
    came_from = {}

    while queue:
        current = queue.pop(0)
        (r, c), (x, y) = current
        prev = came_from.get(current)
        char = grid[x][y]
        directions = next_direction((r, c), current, char, hw)

        for direction in directions:
            if not contains(seen, direction):
                seen.add(direction)
                queue.append(direction)
                came_from[direction] = current

        mapper[x][y] += 1
        if mapper[x][y] == 1:
            count += 1
    return count 


def solve_part_one(grid):
    return move_beam(grid, (0, 1), (0, 0))

def solve_part_two(grid):
    l = len(grid)
    count = 0
    for i in range(l):
        count = max(count, move_beam(grid, (0, 1), (i, 0))) 
        count = max(count, move_beam(grid, (0, -1), (i, l-1))) 
        count = max(count, move_beam(grid, (1, 0), (0, i))) 
        count = max(count, move_beam(grid, (-1, 0), (l-1, i))) 
    return count

if __name__ == '__main__':
    data = read_data('./data/2023/day16_input.txt')
    result = solve_part_one(data)
    pt_result = solve_part_two(data)
    print('PART ONE', result)
    print('PART TWO', pt_result)
