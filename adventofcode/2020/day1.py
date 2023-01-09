from itertools import combinations
from read_file import read_data

def part_one(nums):
    result = 0
    for x in nums:
        for y in nums & {2020 - x}:
            if x != y:
                result = x * y
    if result:
        return result

def part_two(nums):
    result = 0

    for x, y in combinations(nums, 2):
        for z in nums & {2020 - x - y}:
            result = x * y * z
    if result:
        return result

if __name__ == '__main__':
    filename = '../data/day1_input.txt'
    d = set(read_data(filename, int)) 
    result = part_one(d), part_two(d)
    print(result)

