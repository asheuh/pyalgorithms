class Vector:
    def __init__(self, x=None, y=None, height=None, width=None):
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
            'R': (0, 1),
            'L': (0, -1),
            'D': (1, 0),
            'U': (-1, 0)
        }
        if key == 'all':
            directions['NW'] = (-1, 1)
            directions['NE'] = (1, 1)
            directions['SW'] = (-1, -1)
            directions['SE'] = (1, -1)
        return directions

    def contains(self, iterable, node):
        for item in iterable:
            if item == node:
                return True
        return False


def neighbouring_vectors(coords, h, w, key):
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

def create_map(grid, key='all'):
    mapp = {}
    h = len(grid) # height
    w = len(grid[0]) # width

    for x, row in enumerate(grid):
        for y, point in enumerate(row):
            neighbours = neighbouring_vectors((x, y), h, w, key)
            mapp[point] = ((x, y), neighbours)
    return mapp
