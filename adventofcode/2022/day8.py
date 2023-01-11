import math

from read_file import read_data

from time import sleep
from functools import reduce

def find_max(counts):
    return reduce(lambda x, y: x * y, counts)

def check_visibility(start, h, w, is_part2):
    direction = {
        'left': (-1, 0),
        'right': (0, 1),
        'up': (1, 0),
        'down': (0, -1)
    }
    counts = []
    for dir in direction:
        i, j = direction[dir]
        r, c = start
        x, y = (i + r), (j + c)
        is_visible = True # Assume it is visible
        count = 0

        while (x >= 0 and x < h) and (y >= 0 and y < w):
            if forest[x][y] >= forest[r][c]:
                is_visible = False
                count += 1
                break
            x, y = (x + i, y + j)
            count += 1

        if is_part2:
            counts.append(count) # viewing distance

        if is_visible and not is_part2:
            break
    if is_part2:
        return find_max(counts)
    return is_visible

def find_visibility(forest, is_part2=False):
    H = len(forest)
    W = len(forest[0])
    visible_trees = (H * 2) + ((W - 2) * 2) # Trees on the edge are visible by default
    st = 1
    scenic_score = -math.inf

    for i in range(st, H - st):
        for j in range(st, W - st):
            start = (i, j)
            res = check_visibility(start, H, W, is_part2)
            if is_part2:
                if res > scenic_score:
                    scenic_score = res
                    
            if not is_part2 and res:
                visible_trees += 1
    if is_part2:
        return scenic_score
    return visible_trees

if __name__ == '__main__':
    forest = read_data('../data/2022/forest_input.txt')
    res = find_visibility(forest, True)
    print(res)
