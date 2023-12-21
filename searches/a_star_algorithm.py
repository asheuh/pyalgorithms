import math

from heapq import heappush, heappop
from collections import defaultdict
from typing import List, Any

from python.pyalgorithms.utils import neighbouring_vectors


class AStarAlgorithm:
    def __init__(self, start=None, goal=None, grid=None):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])

    @staticmethod
    def contains(iterable: List[Any], item):
        for value in iterable:
            if value == item:
                return True
        return False

    @staticmethod
    def heury(n, g):
        # heuristic function, manhattan distance
        x, y = n
        x1, y1 = g
        d = abs(x1 - x) + abs(y1 - y)
        return d

    def distance(self, n):
        nx, ny = n
        d = self.grid[nx][ny]
        assert int(d)
        return int(d)

    def get_neighbouring_vectors(self, current, where=None):
        return neighbouring_vectors(current, self.h, self.w)

    def algorithm(self):
        heap = [(self.start, (0, 0))] # Initialize start with zero cost
        came_from = {}

        # For node n, g_score[n] is the cost of the cheapest path from start to n currently known.
        g_score = defaultdict(int)
        g_score[self.start] = 0

        # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
        # how cheap a path could be from start to finish if it goes through n.
        f_score = defaultdict(int)
        f_score[self.start] = self.heury(self.start, self.goal)
        seen = set()
        
        while heap:
            current, where = heappop(heap)
            cost = g_score[current]

            if current == self.goal:
                total_path = [current]
                while current in came_from:
                    current = came_from[current]
                    total_path = [*[current], *total_path]
                return total_path, cost 

            neighbours = self.get_neighbouring_vectors(current, where)
            
            for ww, nr in neighbours:
                child = (nr.x, nr.y)
                if child not in g_score:
                    g_score[child] = math.inf

                # d(current, child) is the weight of the edge from current to child
                t_score = g_score[current] + self.heury(current, child)
                if t_score < g_score[child]:
                    came_from[child] = current
                    g_score[child] = t_score
                    f_score[child] = t_score + self.heury(child, self.goal)

                    if not self.contains(heap, child):
                        heappush(heap, (child, ww))
        return 'Failed', 0
