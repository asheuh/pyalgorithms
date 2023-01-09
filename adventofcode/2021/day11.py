import pprint, re
from time import sleep

from read_file import read_data
from helpers import Vector, neighbouring_vectors, create_map

def part_one(energy_levels, is_part2=False):
    grid = energy_levels
    mapp = create_map(grid, 'dumbo')
    total_count = 0
    step = 0

    while True:
        explored = []
        count = 0

        for coord, value_neighbours in mapp.items():
            value, neighbours = value_neighbours
            value += 1
            if coord in explored:
                continue

            if value > 9:
                stack = [coord]

                while stack:
                    x, y = stack.pop() 
                    v, nns = mapp[(x, y)]

                    for nn in nns: 
                        nx, ny = (nn.x, nn.y)
                        nv, nnns = mapp[(nx, ny)] 

                        if (nx, ny) in explored:
                            continue
                        
                        nvalue = nv + 1

                        if nvalue > 9:
                            stack.append((nx, ny))
                            count += 1
                            nvalue = 0

                        mapp[(nx, ny)] = (nvalue, nnns)
                        grid[nx][ny] = nvalue

                    grid[x][y] = 0
                    mapp[(x, y)] = (0, nns)
                    explored.append((x, y))
                value = 0
                count += 1
            mapp[coord] = (value, neighbours)
            grid[coord[0]][coord[1]] = value
        total_count += count # part one

        if len(mapp) == len(explored): # part two
            pprint.pprint(grid)
            step += 1
            break

        step += 1

#         step += 1
#         if step >= steps:
#             break
    if not is_part2:
        return total_count
    return total_count, step

def part_two(energy_levels):
    return part_one(energy_levels, True)

def parser(section):
    return [i for i in section] 


if __name__ == '__main__':
    data = read_data('data/2021/day11_input.txt', parser=parser)
#     result_p1 = part_one(data, 100)
    result_p2 = part_two(data)
#     print(result_p1)
    print(result_p2)
