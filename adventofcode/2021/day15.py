import pprint
import math

from heapq import *
from collections import defaultdict
from time import sleep

from read_file import read_data
from helpers import *


def part_one(maps_risk_levels):
    """Solve using Dijkstra's algorithm"""
    maps_risk_levels = process_data(maps_risk_levels) # part two

    def contains(iterable, nd):
        for item in iterable:
            if item == nd:
                return True
        return False

    def heury(node, goal):
        # heuristic function, manhattan distance
        x, y = node
        x1, y1 = goal
        d = abs(x1 - x) + abs(y1 - y)
        return d

    def dist(mapp, neighbor):
        nx, ny = neighbor
        return int(mapp[nx][ny])

    h = len(maps_risk_levels)
    w = len(maps_risk_levels[0])
    start, goal = (0, 0), (h - 1, w - 1)
    heap, explored = [], []
    heappush(heap, (0, start)) # initialize start with 0 cost
    came_from = {}
    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    g_score = defaultdict(int) 
    g_score[start] = 0
    result = None

    while heap:
        cost, current = heappop(heap)

        if current == goal:
            total_path = [current]
            while current in came_from:
                current = came_from[current]
                total_path = [*[current], *total_path]
            result = total_path
            break

        neighbors = neighbouring_vectors(current, h, w)

        for nr in neighbors:
            child = (nr.x, nr.y)
            if child not in g_score:
                g_score[child] = math.inf

            # d(current, child) is the weight of the edge from current to child
            t_g_score = g_score[current] + dist(maps_risk_levels, child)
            if t_g_score < g_score[child]:
                came_from[child] = current
                g_score[child] = t_g_score
                if not contains(explored, child) and not contains(heap, child):
                    heappush(heap, (t_g_score, child))
    total_rl = 0
    for ccc in result:
        r, c = ccc
        if ccc != start:
            ress = maps_risk_levels[r][c]
            total_rl += int(ress)
    return total_rl


if __name__ == '__main__':
    data = read_data('data/2021/day15_input.txt')
    result_p1 = part_one(data)
    print(result_p1)
