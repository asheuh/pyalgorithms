import re

from functools import reduce

from read_file import read_data


def parser(line):
    return re.findall(r'\d+', line)

def parse_int(items):
    return [int(i) for i in items]

def solve(data, is_part_two=False):
    if is_part_two:
        data = [[int(''.join(i))] for i in data]
    else:
        data = [parse_int(i) for i in data]

    time, distance = data
    result = 1

    for i, t in enumerate(time):
        record = distance[i]
        count = 0

        for _t in range(1, t + 1):
            k = _t * (t-_t)
            if k > record:
                count = _t
                break

        f = t - count
        c = (f - count) + 1
        result *= c
    return result


if __name__ == '__main__':
    data = read_data('./data/2023/day06_input.txt', parser=parser)
    result = solve(data)
    print('PART ONE: ', result)
    pt_result = solve(data, True)
    print('PART TWO: ', pt_result)
