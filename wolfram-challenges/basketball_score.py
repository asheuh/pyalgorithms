# Problem: https://challenges.wolframcloud.com/challenge/getting-a-basketball-score

from time import sleep
from typing import List


def basketball_score(n: int):
    count = 0
    temp = n
    results = []
    while n:
        if n == 3 or n == 2:
            twos = [2] * (count)
            results.append(twos + [n])
            break

        if n % 3 == 0:
            twos = [2] * count
            threes = [3] * (n // 3)
            results.append(twos + threes)

        n -= 2
        count += 1
    return results

def verifiy(items: List[int], n: int) -> List[bool]:
    return [sum(i) == n for i in items]


if __name__ == '__main__':
    n = 19
    res = basketball_score(n)
    print(verifiy(res, n))
    print(res)
