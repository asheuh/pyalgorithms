import re

from read_file import read_data


def parser(line):
    return [int(i) for i in re.findall(r'[-+]?\d+', line)]

def solve(report, is_part_two=False):
    total = 0
    for rp in report:
        total += get_prediction(rp, is_part_two)
    return total

def get_prediction(report, is_part_two):
    i, j = 0, 1
    n = len(report)
    last = [report[-1]]
    first = [report[0]]
    sequence = []

    while i < n:
        diff = report[j] - report[i]
        sequence.append(diff)
        i += 1
        j = i + 1

        if j >= n:
            last.append(sequence[-1])
            first.append(sequence[0])
            if not any(sequence):
                break

            i, j, n = 0, 1, len(sequence)
            report = sequence
            sequence = []
    if is_part_two:
        return predict_first(first)
    return sum(last)

def predict_first(first):
    result = 0
    total = 0
    for i in range(len(first) - 1, -1, -1):
        f = first[i]
        result = f - result
    return result


if __name__ == '__main__':
    data = read_data('./data/2023/day09_input.txt', parser=parser)
    result = solve(data)
    print('PART ONE ', result)
    pt_result = solve(data, True)
    print('PART TWO ', pt_result)
