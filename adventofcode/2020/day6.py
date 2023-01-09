import re
from read_file import read_data


def part_one(groups):
    return sum(groups)

def parse_one(group):
    g = set(re.sub(r'\n+', '', group))
    return len(g)


def parse_two(group):
    g = group.split('\n')
    k = set(g[0])
    # set.intersection 
    for item in g:
        k &= set(item)

    return len(k)


def part_two(groups):
    return sum(groups)


if __name__ == '__main__':
    filename = '../data/day6_input.txt'
    d1 = read_data(filename, parser=parse_one, sep='\n\n')
    d2 = read_data(filename, parser=parse_two, sep='\n\n')
    result = part_one(d1), part_two(d2)
    print(result)
