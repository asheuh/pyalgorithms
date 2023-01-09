import re
from typing import List, Tuple
from read_file import read_data


def part_one(commands: List[Tuple], with_aim: bool=False) -> int:
    helpers = {
        'forward': ('horizontal', lambda x, y: x + y),
        'down': ('vertical', lambda x, y: x + y),
        'up': ('vertical', lambda x, y: x - y)
    }
    horizontal = 0
    depth = 0

    # part two
    if with_aim:
        aim = 0

    for command in commands:
        direction, units = command
        key, f = helpers[direction]
        u = int(units)
        
        if key == 'horizontal':
            # part two
            if with_aim:
                horizontal = f(horizontal, u)
                depth = f(depth, (aim * u))
                continue
            horizontal = f(horizontal, u)
        else:
            # part two
            if with_aim:
                aim = f(aim, u)
                continue
            depth = f(depth, u)
            
    return (horizontal * depth)

def part_two(commands: List[Tuple[str, str]]) -> int:
    return part_one(commands, True)

def parser(command):
    return tuple(re.findall(r'(\w+)', command))


if __name__ == '__main__':
    data = read_data('../data/2021/day2_input.txt', parser)
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1, result_p2)

