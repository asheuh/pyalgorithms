# Problem: https://challenges.wolframcloud.com/challenge/odds-before-evens

from typing import List


def odds_b4_evens(numbers: List[int]) -> List[int]:
    odds = []
    evens = []
    for num in numbers:
        if num & 1:
            odds.append(num)
        else:
            evens.append(num)

    return odds + evens


if __name__ == '__main__':
    numbers = [-1, 2, 8, -9, -2, -3, -6, -10, -8, 5, 7, 9, 7] 
    res = odds_b4_evens(numbers)
    print(res)
