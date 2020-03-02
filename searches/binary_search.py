import time
import math


def binary_search(a: list, k) -> bool:
    """
    > binary_search([1, 4, 6, 2, 4, 8, 5, 7], 6)
    True
    > binary_search([1, 4, 6, 2, 4, 8, 5, 7], 10)
    False
    """
    a = sorted(a)
    l = 1
    u = len(a)

    found = False

    while not found:
        i = (l + u) >> 1
        ki = a[i]
        if u < l:
            break
        if k < ki:
            u = i - 1
        elif k > ki:
            l = i + 1
        else:
            found = True
    return found


def uniform_binary_search(a: list, k) -> bool:
    a = sorted(a)
    N = len(a)
    i = math.ceil(N / 2)
    m = math.floor(N / 2)
    found = False

    while not found:
        ki = a[i]
        if k < ki:
            if m == 0:
                break
            else:
                i -= math.ceil(m / 2)
                m = math.floor(m / 2)
        elif k > ki:
            if m == 0:
                break
            else:
                i += math.ceil(m / 2)
                m = math.floor(m / 2)
        else:
            found = True
    return found


def uniform_binary_search_alt(a: list, k) -> bool:
    """
    Same as uniform_binary_search() but uses an auxiliary table
    in place of the calculations involving m
    2 times faster than binary_search()
    """
    a = sorted(a)
    N = len(a)
    found = False

    d = math.floor(math.log(N, 2)) + 2
    DELTA = [0] * N

    for j in range(1, d):
        v = (N + 2**j - 1) / 2**j
        DELTA[j] = math.floor(v)

    i, j = DELTA[1], 2

    while not found:
        ki = a[i]
        if k < ki:
            if DELTA[j] == 0:
                break
            else:
                i -= DELTA[j]
                j += 1
        elif k > ki:
            if DELTA[j] == 0:
                break
            else:
                i += DELTA[j]
                j += 1
        else:
            found = True
    return found


if __name__ == "__main__":
    a = [12, 32, 42, 100, 14, 56, 34, 58, 78, 96, 83, 63, 71, 18, 19, 86]

    start = time.time()
    found = binary_search(a, 78)
    elapsed = time.time() - start
    print(elapsed)

    s = time.time()
    f = uniform_binary_search_alt(a, 78)
    e = time.time() - s

    print(e)
    print(f)
