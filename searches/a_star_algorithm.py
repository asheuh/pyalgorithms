import math

from heapq import heappush, heappop
from collections import defaultdict
from typing import List, Any

from python.pyalgorithms.utils import neighbouring_vectors


class AStarAlgorithm:
    @staticmethod
    def contains(iterable: List[Any], item):
        for value in iterable:
            if value == item:
                return True
        return False

    @staticmethod
    def heury(node, goal):
        # heuristic function, manhattan distance
        x, y = node
        x1, y1 = goal
        d = abs(x1 - x) + abs(y1 - y)
        return d

    @staticmethod
    def distance(mapp, neighbour):
        nx, ny = neighbour
        return mapp[nx][ny]

    def algorithm(self, start, goal, hw):
        heap = []
        h, w = hw
        heappush(heap, (0, start)) # Initialize start with zero cost
        came_from = {}
        # For node n, g_score[n] is the cost of the cheapest path from start to n currently known.
        g_score = defaultdict(int)
        g_score[start] = 0
        result = None

        # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
        # how cheap a path could be from start to finish if it goes through n.
        f_score = defaultdict(int)
        f_score[start] = self.heury(start, goal)
        
        while heap:
            cost, current = heappop(heap)

            if current == goal:
                total_path = [current]
                while current in came_from:
                    current = came_from[current]
                    total_path = [*[current], *total_path]
                return total_path

            neighbours = neighbouring_vectors(current, h, w)
            
            for nr in neighbours:
                child = (nr.x, nr.y)
                if child not in g_score:
                    g_score[child] = math.inf

                # d(current, child) is the weight of the edge from current to child
                t_score = g_score[current] + self.heury(current, child)
                if t_score < g_score[child]:
                    came_from[child] = current
                    g_score[child] = t_score
                    f_score[child] = t_score + self.heury(child, goal)

                    if not self.contains(heap, child):
                        heappush(heap, (t_score, child))
        return 'Failed'
