import pprint
from collections import defaultdict

from read_file import read_data

def part_one(mapp):
    start = []
    end = []
    path_map = defaultdict(list)
    print(mapp)

    for path in mapp:
        if 'start' in path:
            s_index = path.index('start')
            start.append(path[s_index - 1])
        elif 'end' in path:
            e_index = path.index('end')
            end.append(path[e_index - 1])
        else:
            a, b = path
            path_map[a].append(b)

    number_of_paths = 0 

    for cave in start:
        nodes = path_map[cave]


def parser(section):
    return tuple(section.split('-')) 


if __name__ == '__main__':
    data = read_data('data/2021/day12_input.txt', parser=parser)
    result_p1 = part_one(data)
    print(result_p1)
