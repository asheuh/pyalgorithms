import re, pprint

from collections import defaultdict

from read_file import read_data


def part_one(dots, grid):
    coordinates, folds = dots
    coordinates = [tuple(int(v) for v in re.findall(r'\d+', coord))
            for coord in coordinates]
    folds = [tuple(re.findall(r'\w=[0-9]+', fold)[0].split('=')) for fold in folds]
    visible_dots = len(coordinates)
    done_map = {coord: i for i, coord in enumerate(coordinates)}
    seen = {}

    for fold in folds:
        vector, value = fold
        v = int(value)
        stack = defaultdict(list)

        for coord in coordinates:
            j, k = coord
            try:
                if vector == 'y':
                    a = k
                    b = seen[j]
                    seen[j] = k
                    L = stack[j]
                    cc = (j, b)
                    
                    if k > v: # part two
                        nx, ny = j, (v - (k - v))
                        index = done_map[(j, k)]
                        del done_map[(j, k)]
                        done_map[(nx, ny)] = index
                        continue
                else:
                    a = j
                    b = seen[k]
                    seen[k] = j
                    L = stack[k]
                    cc = (b, k) 
                    
                    if j > v: # part two
                        nx, ny = (v - (j - v)), k
                        index = done_map[(j, k)]
                        del done_map[(j, k)]
                        done_map[(nx, ny)] = index
                        continue

                if abs(a - v) == abs(b - v):
                    # part two
                    st = ['', '']
                    mini = min(a, b)
                    mini_index = cc.index(mini)
                    st[mini_index] = mini
                    st[mini_index - 1] = cc[mini_index - 1]
                    cod = tuple(st)
                    del done_map[cod]
                    visible_dots -= 1
                    continue
                
                i = 0
                n = len(L)
                while i < n:
                    x, y = L[i]
                    if vector == 'y':
                        s = k
                        t = y
                    else:
                        s = j
                        t = x

                    if abs(s - v) == abs(t - v):
                        # part two
                        st2 = ['', '']
                        mini2 = min(s, t)
                        mini_index2 = cc.index(mini2)
                        st[mini_index2] = mini2
                        st[mini_index2 - 1] = cc[mini_index2 - 1]
                        cod2 = tuple(st2)
                        del done_map[cod2]
                        visible_dots -= 1
                        break
                    i += 1

                if vector == 'y':
                    stack[j].append((j, b))
                else:
                    stack[k].append((b, k))
            except Exception as e:
                if vector == 'y':
                    seen[j] = k
                    if k > v: # part two
                        nx, ny = j, (v - (k - v))
                        index = done_map[(j, k)]
                        del done_map[(j, k)]
                        done_map[(nx, ny)] = index
                else:
                    seen[k] = j
                    if j > v: # part two
                        nx, ny = (v - (j - v)), k
                        index = done_map[(j, k)]
                        del done_map[(j, k)]
                        done_map[(nx, ny)] = index
        coordinates = [key for key, val in done_map.items()]

    for key in coordinates:
        x1, y1 = key
        grid[y1][x1] = '#'

    for row in grid:
        print(''.join(row))
    return visible_dots

def parser(section):
    return section.split('\n')

def p(sec):
    return [i for i in sec]


if __name__ == '__main__':
    data = read_data('data/2021/day13_input.txt', parser=parser,  sep='\n\n')
    grid = read_data('data/2021/grid.txt', parser=p)
    result_p1 = part_one(data, grid)
    print(result_p1)
