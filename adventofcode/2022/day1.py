import math

from typing import List

from read_file import read_data


def _calories(data: List[List[str]]) -> iter:
    return map(sum, data)

def max_calories(data: List[List[str]]) -> iter:
    return max(_calories(data))

def top_three(data: List[List[str]], counter: int) -> int:
    first_3 = sorted(_calories(data), reverse=True)[:counter]
    return sum(first_3)

def parser(string: str) -> List[int]:
    return [int(c) for c in string.split('\n')] 


if __name__ == '__main__':
    data = read_data('../data/2022/calories_input.txt', parser=parser, sep='\n\n')
    # part one
    one = max_calories(data)
    # part_two
    two = top_three(data, 3)
    print(two)
