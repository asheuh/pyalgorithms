import math
from collections import Counter
from read_file import read_data

def part_one(positions, is_constant_rate=True):
    n = len(positions) 
    counter = Counter(positions)
    total_fuel = math.inf

    for i in range(1, n + 1):
        i_fuel = 0
        for pos, count in counter.items():
            diff = abs(pos - i)

            if not is_constant_rate: # part two
                diff = diff * (diff + 1) // 2 # summation i.e 1-->10 1+2+3+4+5+6+7+8+9+10=55

            i_fuel += (diff * count)

        if i_fuel < total_fuel:
            total_fuel = i_fuel
#         print(f'Position {positions[i - 1]} => {i} = {diff}')
    return total_fuel


def part_two(positions):
    return part_one(positions, False)


if __name__ == '__main__':
    data = read_data('data/2021/day7_input.txt', parser=int, sep=',')
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1, result_p2)
