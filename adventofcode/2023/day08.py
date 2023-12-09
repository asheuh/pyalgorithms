import re

from read_file import read_data
import pprint


def parser(line):
    return line.split('\n')

def solve_part_one(data):
    directions = [0 if d == 'L' else 1 for d in data[0][0]]
    mapper = create_map(data[1])
    start, target, count, i = 'AAA', 'ZZZ', 0, 0
    to = mapper.get(start)
    if not to:
        return 0

    n = len(directions)
    
    while i < n:
        dr = directions[i]
        start = to[dr]
        count += 1

        if start == target:
            break
        
        to = mapper[start]
        i += 1
        if i >= n: # reset directions
            i = 0

    return count

def get_start_nodes(mapper):
    for node in mapper:
        if node.endswith('A'):
            yield node


def solve_part_two(data):
    directions = [0 if d == 'L' else 1 for d in data[0][0]]
    mapper = create_map(data[1])
    start_nodes = get_start_nodes(mapper) 
    n = len(directions)
    i, count = 0, 0 # Count is 1 because of step 0

    while i < n:
        dr = directions[i]
        new_start_nodes = []
        _all = 0

        for start in start_nodes:
            to = mapper[start][dr]
            if to.endswith('Z'):
                _all += 1

            new_start_nodes.append(to)

        if _all == len(new_start_nodes):
            break

        start_nodes = new_start_nodes
        i += 1
        count += 1

        if i >= n:
            i = 0
    return count

def create_map(maps):
    mapper = {}

    for m in maps:
        key, value = m.split(' = ')
        x = re.findall(r'(\w+), (\w+)', value)[0]
        mapper[key] = x
    return mapper


if __name__ == '__main__':
    data = read_data('./data/2023/day08_input.txt', sep="\n\n", parser=parser)
    result = solve_part_one(data)
    print('PART ONE ', result)
    pt_result = solve_part_two(data)
    print('PART TWO ', pt_result)
