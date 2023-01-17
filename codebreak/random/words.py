import math

from time import time

def solve(arr: list):
    maps = {}
    maxm = 0
    www = tuple()

    for i in range(len(arr)):
        word = arr[i]

        for j in range(len(arr)):
            w = arr[j]

            if not set(word) & set(w):
                length = len(word) * len(w)

                if length > maxm:
                    maxm = length
                    www = (word, w)
    return maxm, www

def solution(arr):
    def is_empty(s):
        return len(s) == 0

    first = arr[0]
    queue = [first]
    i = 0
    m = -math.inf
    www = tuple()

    while not is_empty(queue):
        word = queue[0]
        queue = queue[1:]

        neighbours = arr[i + 1:]

        for item in neighbours:
            if not set(word) & set(item):
                l = len(word) * len(item)

                if l > m:
                    www = (word, item)
                    m = l

            if item not in queue:
                queue.append(item)
        i += 1
    return m, www

def car_parking(arr, k):
    n = len(arr)
    arr.sort()

    i = 0
    min_diff = math.inf
    k = k - 1

    while i < n and k < n:
        first = arr[i]
        last = arr[k]
    
        diff = last - first

        if diff < min_diff:
            min_diff = diff

        i += 1
        k += 1
    return min_diff + 1

def parse_grid(h, w):

    for i in range(h):
        for j in range(w):
            print(i, j, grid[i][j])


class Node:
    def __init__(self, root, state: tuple):
        self.state = state
        self.root = root

def reachTheEnd(grid, k):
    h = len(grid)
    w = len(grid[0])
    start = (0, 0)
    goal = (h - 1, w - 1)

    def is_empty(s):
        return len(s) == 0

    def neighbours(coord):
        r, c = coord
        directions = {
                'N': (0, 1),
                'S': (0, -1),
                'W': (-1, 0),
                'E': (1, 0)
                }

        n_bours = []

        for direction in directions:
            x, y = directions[direction]
            row, col = r + x, c + y

            if h > row >= 0 and w > col >= 0:
                agent = grid[row][col]

                if agent != '#':
                    n_bours.append((row, col))

        return n_bours

    
    def contains(state, iterable):
        for item in iterable:
            if item.state == state:
                return True
        return False


    node = Node(state=start, root=None)
    queue = [node]
    explored = list()
    count = 0

    while not is_empty(queue):
        node = queue[0]
        queue = queue[1:]
        print(node.state, goal)

        if node and node.state == goal:
            explored = []

            while node.root:
                explored.append(node.state)
                count += 1
                node = node.root
            break

        n = neighbours(node.state)

        for c in n:
            if not contains(c, queue) and not contains(c, explored):
                child = Node(state=c, root=node)
                queue.append(child)
        explored.append(node)

    if count <= k:
        return 'YES', count
    return 'NO', count
 

if __name__ == '__main__':
    data = open('input_yes.txt', 'r').read().rstrip().split('\n')
    grid = data 
    mt = 5
    r = reachTheEnd(grid, mt)
    print(r)
#     T = int(input())
#     contents = open('input003.txt').read().rstrip().split('\n')
# 
#     arr = list(map(int, contents))[1:]
#     k = arr.pop()
#     r = car_parking(arr, k)
#     print(r)
#     arr = ['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef']
#     t = time()
#     r = solution(arr)
#     e = time() - t
# 
#     t1 = time()
#     res = solve(arr)
#     e1 = time() - t1
# 
#     print(r, 'BFS', e)
#     print(res, 'BRUTAL', e1)
