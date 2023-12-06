import re
import math

from time import sleep
from itertools import chain
from collections import defaultdict

from read_file import read_data
import pprint

def aintegers(_string):
    return [int(i) for i in re.findall(r'\d+', _string)] 

def remove_map(name):
    return name.replace(" map", "")

def parser(line):
    name_map = {}
    name, values = line.split(":")
    name_map[remove_map(name)] =  [aintegers(i) for i in values.split("\n") if i]
    return name_map

def parse_map(key, values):
    parsed_map = defaultdict(list)

    for i, value in enumerate(values):
        dest, src, length = value
        k, v = key.split('-to-')
        src_range = range(src, src + length)
        dest_range = range(dest, dest + length)
        parsed_map[key] += [(src, dest), (src + length - 1, dest + length - 1)]
    return parsed_map

def map_seeds(seeds, is_part_two):
    if not is_part_two:
        return [(a, ) for a in seeds]

    f = [c for i, c in enumerate(seeds) if not i & 1]
    s = [c for i, c in enumerate(seeds) if i & 1]
    return list(zip(f, s))

def create_map(almanac, is_part_two):
    mapper = {}

    for al in almanac:
        for key, value in al.items():
            if key.lower() == 'seeds':
                mapper[key.lower()] = map_seeds(value[0], is_part_two)
            else:
                mapper.update(parse_map(key, value))
    return mapper

def get_location(seed, mapped, is_part_two):
    stack = [seed]
    keys = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]
    prev = seed

    while stack:
        prev = stack.pop()

        for key in keys:
            ranges = mapped.get(key, {})
            start = [item for i, item in enumerate(ranges) if not i & 1]
            end = [item for i, item in enumerate(ranges) if i & 1]
            x = prev[0] 

            for j in range(len(start)):
                j_start = start[j]
                j_end = end[j]
                f_j_start, val_start = j_start
                f_j_end, val_end = j_end

                if not (f_j_start <= x <= f_j_end):
                    continue

                # Find the value of interest
                # Part two 
                k = sum(prev)
                p = prev
                prev = ((x - f_j_start) + val_start, )

        if is_part_two:
            pass
    return prev

def solve(almanac, is_part_two=False):
    mapped = create_map(almanac, is_part_two)
    seeds = mapped.get('seeds')
    lowest = math.inf

    for seed in seeds:
        location, = get_location(seed, mapped, is_part_two)
        if location < lowest:
            lowest = location
    return lowest


if __name__ == '__main__':
    data = read_data('../data/2023/day05_input.txt', parser=parser, sep="\n\n")
    result = solve(data)
    print('PART ONE: ', result)
    pt_result = solve(data, True)
    print('PART TWO: ', pt_result)
