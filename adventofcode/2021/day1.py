from read_file import read_data
from time import sleep

def part_one(measurements):
    total_increases = 0
    stack = []

    for measure in measurements:
        try:
            previous = stack.pop()
        
            diff = measure - previous

            if diff > 0:
                total_increases += 1
            stack.append(measure)
        except Exception as e:
            stack.append(measure)
    return total_increases


def part_two(m):
    """
    params: m -> list
        m is the measurements
    return: total_inc -> int
        total_inc is the total_increase between previous and current value
    """
    n = len(m)
    left = 0
    right = 1
    stack = []
    total_inc = 0

    # n - 1 since we are sliding in threes and by the time we get to n - 1 we will have completed all the values
    while right < (n - 1):
        a, b, c = m[left: right + 2]
        cur_sum = sum([a, b, c])

        try:
            prev_sum = stack.pop()
            if (cur_sum - prev_sum) > 0:
                total_inc += 1
            stack.append(cur_sum)
        except Exception as e:
            stack.append(cur_sum)
        left += 1
        right += 1

    return total_inc


if __name__ == '__main__':
    data = read_data('../data/2021/day1_input.txt', int)
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1, result_p2)
# 
