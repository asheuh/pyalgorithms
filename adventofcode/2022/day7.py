import re
import pprint

from read_file import read_data

from time import sleep
from collections import defaultdict


def find_total(items, is_part2=False):
    limit = 100000
    total = 0
    dirs = ['/']
    sizes = defaultdict(int)

    i = 0
    n = len(items)
    while i < n:
        item = items[i]
        if re.findall(r'\d+', item):
            number = re.findall(r'\d+', item)
            num = int(number[0])
            for dirr in dirs:
                sizes[dirr] += num

        elif item.startswith('$') and 'cd' in item:
            _, cd, d = item.split(' ')
            if d == '/':
                dirs = ['/']
            elif d == '..':
                dirs.pop()
            else:
                dirs.append(dirs[-1] + d + '/')
        i += 1
    
    # part two
    if is_part2:
        available_mem = 70000000
        required_mem = 30000000
        unused_mem = available_mem - sizes['/']
        mins = []

        for dir in sizes:
            value = sizes[dir] 
            if value + unused_mem >= required_mem:
                mins.append(value)
        return min(mins)
    return sum(v for v in sizes.values() if v <= limit)


if __name__ == '__main__':
    data = read_data('../data/2022/output_input.txt')
    res = find_total(data, True)
    print(res)
