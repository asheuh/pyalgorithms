class Node:
    def __init__(self, state, root=None):
        self.state = state
        self.root = root


class Vector:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def plus(self, other, x, y):
        # Addition to get the next a adjacent
        return Vector(other.x + x, other.y + y, self.height, self.width)

    def is_inside(self):
        # check if we are still inside the grid
        return 0 <= self.x < self.height and 0 <= self.y < self.width

    def directions(self, key='four'):
        directions = {
            'UP': (0, 1),
            'DOWN': (0, -1),
            'RIGHT': (1, 0),
            'LEFT': (-1, 0)
        }
        if key == 'all':
            directions['NW'] = (-1, 1)
            directions['NE'] = (1, 1)
            directions['SW'] = (-1, -1)
            directions['SE'] = (1, -1)
        return directions


def neighbouring_vectors(coords, h, w, key='four'):
    x, y = coords
    v = Vector(x, y, h, w)
    directions = v.directions(key)
    neighbours = []
    
    for direction in directions:
        x1, y1 = directions[direction]
        new_v = v.plus(v, x1, y1)

        if new_v.is_inside():
            neighbours.append(new_v)
    return neighbours


def process_data(grid):
    # part two of AoC day 15, 2021
    grid1 = []
    grid2 = []
    for line in grid:
        n = len(line)
        to_add = '1' * n
        new_line = line
        temp = line

        for i in range(4):
            tl = temp.replace('9', '0')
            temp = str(int(tl) + int(to_add))
            new_line += temp

        grid1.append(new_line)

    temp_grid = grid1
    for i in range(4):
        ng = []
        for line in temp_grid:
            n = len(line)
            t_add = '1' * n
            line = line.replace('9', '0')
            new_l = str(int(line) + int(t_add))
            ng.append(new_l)
        grid1 += ng
        temp_grid = ng
    return grid1


def create_map(grid, key='four'):
    mapp = {}
    h = len(grid) # height
    w = len(grid[0]) # width

    for x, row in enumerate(grid):
        for y, point in enumerate(row):
            vecs = neighbouring_vectors((x, y), h, w, key)
            if key == 'all' or key == 'chiton':
                mapp[(x, y)] = (int(point), vecs)
            else:
                mapp[(point, (x, y))] = vecs
    return mapp


def contains(iterable, item):
    for it in iterable:
        if it.state == item.state:
            return True
    return False


def find_start_goal(grid, s, g):
    start = None
    goal = None

    for x, row in enumerate(grid):
        for y, point in enumerate(row):
            if point == s:
                start = (x, y)
            if point == g:
                goal = (x, y)
    return start, goal

