import re
from functools import lru_cache
from read_file import read_data

def part_one(data):
    key = 'shiny gold'
    count = 0
    set_lines = set()
    others = list()

    for line in data:
        if not line.startswith(key):
            if key in line:
                count += 1
                first_two = ' '.join(line.split(' ')[:2]) 
                others.append(first_two)
                set_lines.add(line)
        else:
            set_lines.add(line)
        
    for line in data:
        for other in others:
            if other in line and line not in set_lines:
                print(line)
                count += 1
    return count

def parse_bag_rule_norvig(line):
    line = re.sub(r' bags?|[.]', '', line)
    outer, inner = line.split(' contain ')
    result = dict(map(parse_inner_norvig, inner.split(',')))
    return outer, result

def parse_inner_norvig(inner):
    n, bag = inner.split(maxsplit=1)
    return bag, (0 if n == 'no' else int(n))

def part_one_norvig(rules, target):
    @lru_cache(None)
    def contains(bag, target):
        contents = rules.get(bag, {})
        return (target in contents or any(contains(inner, target) for inner in contents))

    count = 0
    for bag in rules:
        if contains(bag, target):
            count += 1
    return count


def part_two():
    pass


if __name__ == '__main__':
    filename = '../data/day7_input.txt'
    data = read_data(filename, parser=parse_bag_rule_norvig)
    result = part_one_norvig(dict(data), 'shiny gold')
    print(result)
