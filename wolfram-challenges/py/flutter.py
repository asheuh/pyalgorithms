from typing import Callable, Any, List

# Problem: https://challenges.wolframcloud.com/challenge/flutter

def flutter(f: Callable, x: Any, items: List[Any]) -> List[Callable]:
    """
    params:
        X = 2
        L = [a, b, c, d]
    returns:
        {f[2, a], f[2, b], f[2, c], f[2, d]}
    """
    results = []
    for item in items:
        results.append(f(x, item))
    return results


def check_equals(x, y):
    return x == y

def subtract(x, y):
    results = []

    for i in x:
        k = i - y
        results.append(k)
    return results


if __name__ == '__main__':
    res = flutter(subtract, [1, 2], [5, 19, 2])
    print(res)
