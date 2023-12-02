import re

from read_file import read_data
from time import sleep

def solve(data):
    total = 0
    map_names_to_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "oneight": 18,
        "twone": 21,
        "threeight": 38,
        "fiveight": 58,
        "sevenine": 79,
        "eightwo": 82,
        "eighthree": 83
    }
    for point in data:
        matches = re.findall(
            r'(oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|one|two|three|four|five|six|seven|eight|nine|\d)',
            point, flags=re.IGNORECASE
        )

        if not matches:
            continue

        matches = ''.join(map(
            lambda x: str(map_names_to_digits[x]) 
            if x in map_names_to_digits else x,
            matches
        ))

        if len(matches) > 1:
            f = matches[0]
            l = matches[-1]
        else:
            f = matches[0]
            l = matches[0]

        assert int(f)
        assert int(l)
        total += int(f'{f}{l}')
    return total


if __name__ == '__main__':
    data = read_data("../data/2023/day1_input.txt")
    result = solve(data)
    print(result)
