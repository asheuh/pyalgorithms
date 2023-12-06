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
    zipped = zip(f, s)
    return [(z[0], sum(z) - 1) for z in zipped]

def create_map(almanac, is_part_two):
    mapper = {}

    for al in almanac:
        for key, value in al.items():
            if key.lower() == 'seeds':
                mapper[key.lower()] = map_seeds(value[0], is_part_two) 
            else:
                mapper.update(parse_map(key, value))
    return mapper

def get_location_part_one(seed, mapped, keys): 
    prev = seed

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
            prev = ((x - f_j_start) + val_start, )
    return prev

def get_location_part_two(seeds, mapped, keys):
    tseeds = seeds

    for key in keys:
        ranges = mapped.get(key, {})
        ranges.sort(key=lambda x: x[0])
        start = [item for i, item in enumerate(ranges) if not i & 1]
        end = [item for i, item in enumerate(ranges) if i & 1]
        stack = []

        for seed in tseeds:
            seed_start, seed_end = seed

            for j in range(len(start)):
                j_start = start[j]
                j_end = end[j]
                f_j_start, val_start = j_start
                f_j_end, val_end = j_end
                possible_start = max(f_j_start, seed_start)

                if possible_start > seed_end:
                    break

                possible_end = min(f_j_end, seed_end)

                if possible_end >= possible_start:
                    if seed_start < possible_start:
                        stack.append((seed_start, possible_start - 1))

                    stack.append((
                        possible_start - (f_j_start - val_start),
                        possible_end - (f_j_start - val_start)
                    ))
                    seed_start = possible_end + 1

            if seed_start < seed_end:
                stack.append((seed_start, seed_end))

        tseeds = stack.copy()
    stack.sort(key=lambda x: x[0])
    return stack[0][0] if stack else None

def solve(almanac, is_part_two=False):
    mapped = create_map(almanac, is_part_two)
    seeds = mapped.get('seeds')
    lowest = math.inf
    keys = [
        'seed-to-soil',
        'soil-to-fertilizer',
        'fertilizer-to-water',
        'water-to-light',
        'light-to-temperature',
        'temperature-to-humidity',
        'humidity-to-location'
    ]

    if is_part_two:
        return get_location_part_two(seeds, mapped, keys)

    for seed in seeds:
        location, = get_location_part_one(seed, mapped, keys)
        if location < lowest:
            lowest = location
    return lowest


if __name__ == '__main__':
    data = read_data('./data/2023/day05_input.txt', parser=parser, sep='\n\n')
    result = solve(data)
    print('PART ONE: ', result)
    pt_result = solve(data, True)
    print('PART TWO: ', pt_result)
