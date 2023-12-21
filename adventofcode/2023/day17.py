import math
import pprint

from heapq import heappush, heappop
from collections import defaultdict

from read_file import read_data
from python.pyalgorithms.searches.a_star_algorithm import AStarAlgorithm
from python.pyalgorithms.utils import Vector


class SubAstar(AStarAlgorithm):
    def __init__(self, grid, start, goal, limit=3, less=0):
        super().__init__(start, goal, grid)
        self.limit = limit
        self.h = len(grid)
        self.w = len(grid[0])
        self.less = less

    def heury(self, n, g):
        return self.distance(g)

    def get_neighbouring_vectors(self, curr, where):
        to = {
            (0, 1): [(1, 0), (-1, 0)],
            (0, -1): [(1, 0), (-1, 0)],
            (1, 0): [(0, 1), (0, -1)],
            (-1, 0): [(0, 1), (0, -1)],
            self.start: [(0, 1), (1, 0)]
        }[where]
        return to 

    def algorithm(self):
        heap = [(0, self.start, (0, 0))] # Initialize start with zero cost
        seen = set()
        g_score = defaultdict(int)
        g_score[(self.start, self.start)] = 0

        while heap:
            cost, current, where = heappop(heap)

            if current == self.goal:
                return None, cost 

            if (current, where) in seen:
                continue
        
            neighbours = self.get_neighbouring_vectors(current, where)
            x, y = current
            v = Vector(x, y, self.h, self.w)

            for t in neighbours:
                c = cost
                a, b = t
                for i in range(1, self.limit + 1):
                    nv = v.plus(v, a*i, b*i)
                    o, p = (nv.x, nv.y)
                    vv = Vector(o, p, self.h, self.w)

                    if not vv.is_inside():
                        continue

                    child = (t, (vv.x, vv.y)) 
                    if child not in g_score:
                        g_score[child] = math.inf

                    # d(current, child) is the weight of the edge from current to child
                    c = c + self.heury(current, child[1])
                    if i >= self.less:
                        if c < g_score[child]:
                            g_score[child] = c
                            heappush(heap, (c, child[1], t))
            seen.add((current, where))
        return None, cost


def solve_part_one(grid):
    l = len(grid) - 1
    astar = SubAstar(grid, (0, 0), (l, l))
    _, cost = astar.algorithm()
    return cost

def solve_part_two(grid, limit, less):
    l = len(grid) - 1
    astar = SubAstar(grid, (0, 0), (l, l), limit=limit, less=less)
    _, cost = astar.algorithm()
    return cost


if __name__ == '__main__':
    grid = read_data('./data/2023/day17_input.txt')
    grid = [list(i) for i in grid]
    result = solve_part_one(grid)
    pt_result = solve_part_two(grid, 10, 4)
    print('PART ONE', result)
    print('PART TWO', pt_result)
