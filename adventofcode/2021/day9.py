import pprint
from time import sleep
from functools import reduce

from read_file import read_data
from helpers import Vector, neighbouring_vectors, create_map


def part_one(heightmap, is_p2=False): 
    grid = heightmap
    h = len(grid) # height
    w = len(grid[0]) # width
    mapp = create_map(grid)
    
    risk_level = 0
    results = []

    for key, value in mapp.items():
        l_h, coords = key # location height and it's coordinates
        n_bours = value # Neighbours
        l_height = int(l_h)

        for n_bour in value:
            nx, ny = n_bour.x, n_bour.y # neighbours coordinates
            n_height = int(grid[nx][ny]) # neighbours height

            if n_height <= l_height:
                l_height = None
                break

        if l_height is not None:
            risk_level += (1 + l_height)

            if is_p2: # Part two
                stack = [coords]
                explored = set()
                while stack:
                    x, y = stack.pop()
                    v = Vector(x, y, h, w)
                    ds = v.directions()

                    if (x, y) not in explored:
                        for k, d in ds.items():
                            r, c = d
                            nv = v.plus(v, r, c)

                            # find all points forming a basin
                            while nv.is_inside() and int(grid[nv.x][nv.y]) < 9:
                                stack.append((nv.x, nv.y))
                                nv = nv.plus(nv, r, c)
                        explored.add((x, y))
                results.append(len(explored))
    largest_basins_result = None
    if results:
        largest_basins_result = reduce(lambda x, y: x * y, sorted(results)[-3:])
    return risk_level, largest_basins_result


def part_two(heightmap):
    return part_one(heightmap, True)


if __name__ == '__main__':
    data = read_data('data/2021/day9_input.txt')
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1[0], result_p2[1])
