import re

from collections import Counter
from time import sleep

from read_file import read_data


def part_one(data, steps):
    template, rules = data[0], data[2:]
    map_rules = {k: v for k, v in rules}
    temp_str = template[0]

    for step in range(steps):
        new_temp = ''
        left = 0
        right = 1
        n = len(temp_str)

        while right < n:
            pair = temp_str[left: right + 1]

            if pair in map_rules:
                element = map_rules[pair]
                seq = ''.join([pair[0], element])
                new_temp += seq

            left += 1
            right += 1
        temp_str = new_temp + pair[1]
    counter = Counter(temp_str)
    return calculate_sub(counter)


def calculate_sub(counter):
    maxx = max(counter.values())
    minn = min(counter.values())
    return maxx - minn


def part_two(data, steps):
    template, rules = data[0], data[2:]
    map_rules = {k: v for k, v in rules}
    temp_str = template[0]
    counter = Counter(temp_str)
    seen = {}
    
    l = 0
    r = 1
    n = len(temp_str)
    # set initial
    while r < n:
        pair = temp_str[l: r + 1]
        try:
            seen[pair] += 1
        except Exception as e:
            seen[pair] = 1
        l += 1
        r += 1

    for step in range(steps):
        new_seen = {} # keep new seen after every step

        for pr in seen:
            count = seen[pr]

            if pr not in map_rules:
                continue

            element = map_rules[pr]
            try:
                counter[element] += count
            except Exception as e:
                counter[element] = 1

            seq = ''.join([pr[0], element])
            seq1 = seq[1]+pr[1]
            
            for sq in (seq, seq1):
                if sq in new_seen:
                    new_seen[sq] += count
                else:
                    new_seen[sq] = count
        seen = new_seen

    return calculate_sub(counter)


def parser(section):
    return tuple(re.findall(r'\w+', section))


if __name__ == '__main__':
    data = read_data('data/2021/day14_input.txt', parser=parser)
    result_p1 = part_one(data, 10) # Super slow
    result_p2 = part_two(data, 40) # Super fast
    print(result_p1, result_p2)
