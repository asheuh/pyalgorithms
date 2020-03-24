"""
imports
"""
from typing import Generator
from time import sleep
from pprint import pprint


def lexco_permutations(_x: str) -> Generator:
    """
    Lexicographic permutation generation
    This algorithm generates all permutations of {w1, w2 ... wn}
    visiting them in lexicographic order

    >>> w = 'bot'
    >>> result = permutations(w)
    >>> result
    >>> ['bot', 'bto', 'obt', 'otb', 'tbo', 'tob', 'obt']

    result
    ------
    The result obtained is in lexicographical order or alphabetincal order
    """
    _n = len(_x) - 1
    pool = list(_x)

    yield "".join(c for c in pool)

    while 1:
        j = _n - 1

        # Find the largest j such that pool[j] can be increased
        while pool[j] >= pool[j + 1]:
            j -= 1

        # Increase pool[j] by the smallest feasible amount
        # in this case pool[l] is the smallest element greater than
        # pool[j] that can legitimately follow pool[0] ... pool[j-1] in a permutation
        _l = _n
        while pool[j] >= pool[_l]:
            _l -= 1
        pool[j], pool[_l] = pool[_l], pool[j]

        # Reverse pool[j+1] ... pool[n]
        # Find the lexicographically least way to extend the new
        # pool[0]...pool[j] to a complete pattern
        k = j + 1
        _c = _n
        while k < _c:
            pool[k], pool[_c] = pool[_c], pool[k]
            k = k + 1
            _c = _c - 1

        if pool != list(w):
            yield "".join(c for c in pool)
        else:
            break
        if j < 0:
            break


def lexperms_reverse(_w: str) -> Generator:
    """
    less efficient but works
    a more effient one is the one the follow(elegant_lexperms_fact())
    """
    _n = len(_w)
    pool = list(_w)

    while _n:
        i = 1
        yield ''.join(c for c in pool)

        while pool[i] <= pool[i - 1]:
            i += 1
            if i >= _n:
                break

        if i >= _n:
            break

        j = 0
        while pool[j] >= pool[i]:
            j += 1

        pool[i], pool[j] = pool[j], pool[i]

        k = i - 1
        _c = 0
        while _c < k:
            pool[k], pool[_c] = pool[_c], pool[k]
            k -= 1
            _c += 1


def elegant_lexperms_fact(_x: str) -> Generator:
    """
    Lexicographic permutations in reverse order
    based on factorial counting(recursion)
    """

    pool = list(_x)
    _l = len(pool)
    _n = _l - 1
    _c = [0] * _l
    i = _n
    _y = _n - 1

    while i > 1:
        _c[i] = 1
        i -= 1

    yield ''.join(c for c in pool)

    while i:
        if i > _n:
            break

        if _c[i] < i:
            if i % 2 != 0:
                _u = 0
            else:
                _u = _c[i]
            if i == _y:
                _u = _c[i]
                i = _n
                print('YES', pool, i, _u, _c)
            if _c[_n] == _n:
                print("FULL", _c, pool, _c[i], i, _u)
            print(pool, i, _u, _c)
            sleep(0.4)
            pool[i], pool[_u] = pool[_u], pool[i]

            k = i - 1
            j = 0
            while j < k:
                pool[j], pool[k] = pool[k], pool[j]
                k -= 1
                j += 1

            _c[i] = _c[i] + 1
            i = 1
            yield ''.join(c for c in pool)
        else:
            _c[i] = 0
            i = i + 1


if __name__ == '__main__':
    T = int(input("Enter number of test cases: "))

    for _ in range(T):
        w = input("Enter value to permute: ")
        r_e_f = list(elegant_lexperms_fact(w))

        #         r_l_r = list(lexperms_reverse(w))

        #         l_p = list(lexco_permutations(w))
        print(f"{'-' * 113}")
        print(r_e_f)
        #         pprint(int(sum(int(n) for n in r_e_f) / len(r_e_f)))
        print(f"{'-' * 113}")
#         print(r_l_r)
#         print("lexperms_reverse", r_l_r)
#         print(f"{'-' * 113}")
#         print("lexco_permutations", l_p)
#         print(f"{'-' * 113}")
