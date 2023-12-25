import math
import pprint

from read_file import read_data
from python.pyalgorithms.utils import *


def filtern(ngs, seen, grid, checks):
    mustgo, obstacle = checks
    must = []
    newn = []
    for nn in ngs:
        x, y = nn.x, nn.y
        is_obstacle = grid[x][y] == obstacle
        is_must = grid[x][y] in mustgo
        is_seen = (x, y) in seen
        if not is_seen and not is_obstacle:
            if is_must:
                must.append((x, y))
            newn.append((x, y))
    return newn if not must else must

def contains(iterable, item):
    for it in iterable:
        if it == item:
            return True
    return False

def solve(grid):
    h = len(grid)
    w = len(grid[0])
    start = 0, get_start_goal(grid[0])
    goal = w-1, get_start_goal(grid[-1])
    mustgo = ['v', '>', '<', '^']
    seen = set()
    results = []
    queue = [start]

    while queue:
        current = queue.pop()
#         queue = queue[1:]

        if current == goal:
            print(queue)
            results.append(len(seen))
            continue

        neighbours = neighbouring_vectors(current, h, w)
        neighbours = filtern(neighbours, seen, grid, (mustgo, '#'))
        print(neighbours)

        for nn in neighbours:
            child = nn

            if not contains(seen, child):
                queue.append(child)
        seen.add(current)

    print('RESULT', results)

def get_start_goal(line):
    return sum(i for i, c in enumerate(line) if c == '.')

def parser(line):
    return [c for c in line]


if __name__ == '__main__':
    data = read_data('./data/2023/day23_input.txt', parser=parser)
    solve(data)
