import pprint

from time import time

from read_file import read_data
from python.pyalgorithms.utils import *


def solve(maze, is_part_two=False):
    mapper = {
        '|': {(-1, 0): ['7', 'F', '|'], (1, 0): ['J', 'L', '|']},
        '-': {(0, 1): ['J', '7', '-'], (0, -1): ['L', 'F', '-']},
        'L': {(0, 1): ['J', '7', '-'], (-1, 0): ['|', '7', 'F']},
        'J': {(-1, 0): ['|', '7', 'F'], (0, -1): ['-', 'L', 'F']},
        'F': {(0, 1): ['J', '7', '-'], (1, 0): ['|', 'J', 'L']},
        '7': {(1, 0): ['J', '|', 'L'], (0, -1): ['F', 'L', '-']},
        'S': {
            (-1, 0): ['|', 'F', '7'],
            (1, 0): ['L', 'J', '|'],
            (0, 1): ['-', '7', 'J'],
            (0, -1): ['-', 'L', 'F']
        }
    }
    h = len(maze)
    w = len(maze[0])
    grid_map, start, goal = create_start_goal(maze)
    stack = [start]
    seen = []
    prev = None

    while stack:
        node = stack.pop(0)

        if prev is not None and node == goal:
            break

        neighbours = grid_map[node]
        neighbours = filter_neighbours(node, neighbours, mapper, maze)

        for n in neighbours:
            if prev == start == n:
                continue

            if not is_contain(stack, n) and not is_contain(seen, n):
                stack.append(n)

        seen.append(node)
        prev = node
    return len(seen) // 2

def is_contain(iterable, item):
    for i in iterable:
        if i == item:
            return True
    return False

def filter_neighbours(node, neighbours, mapper, maze):
    # Filter neighbours
    # 'J': {(0, 1): ['|', '7', 'F'], (-1, 0): ['-', 'L', 'F']},
    h, w = len(maze), len(maze[0])
    neighbours = list((n.x, n.y) for n in neighbours)
    point, (x, y) = node
    tiles = mapper[point]
    new_n = set()
    for key, value in tiles.items():
        v = Vector(x, y, h, w)
        r, c = key
        nv = v.plus(v, r, c)

        if (nv.x, nv.y) not in neighbours:
            continue

        nv_value = maze[nv.x][nv.y]
        if nv_value in value:
            new_n.add((nv_value, (nv.x, nv.y)))
    return new_n

def create_start_goal(maze):
    grid_map, start_goal = create_map(maze, 'S', 'S')
    s, g = start_goal
    start = ('S', s)
    goal = ('S', g)
    return grid_map, start, goal


if __name__ == '__main__':
    data = read_data('./data/2023/day10_input.txt')
    st = time()
    result = solve(data)
    et = time()
    print('PART ONE =>', result)
    print('PART ONE TIME TAKEN =>', et - st)

