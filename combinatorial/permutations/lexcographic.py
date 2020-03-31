"""
imports
"""
from typing import Generator
from time import sleep, time


def lexico_permutations(_x: str) -> Generator:
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
    pool = list(_x)
    n = len(pool)
    last = n - 1

    if n <= 1:
        return

    if n < 3:
        p = reversed(pool)
        yield ''.join(i for i in p)
        return

    yield ''.join(i for i in pool)

    while last:
        j = last - 1

        # Find the largest j such that pool[j] can be increased
        while pool[j] >= pool[j + 1]:
            j = j - 1

        if j < 0:
            break

        # Increase pool[j] by the smallest feasible amount
        # in this case pool[i] is the smallest element greater than
        # pool[j] that can legitimately follow pool[0] ... pool[j-1] in a permutation
        i = last
        while pool[j] >= pool[i]:
            i = i - 1

        pool[j], pool[i] = pool[i], pool[j]

        # Reverse pool[j+1] ... pool[n]
        # Find the lexicographically least way to extend the new
        # pool[0]...pool[j] to a complete pattern
        k = j + 1
        l = last
        while k < l:
            pool[k], pool[l] = pool[l], pool[k]
            k = k + 1
            l = l - 1

        yield ''.join(c for c in pool)


def lexico_permutations_fast(_w: str) -> Generator:
    """
    two times faster than lexco_permutations
    """
    pool = list(_w)
    n = len(pool)
    last = n - 1

    if n <= 1:
        return _w

    yield ''.join(i for i in pool)

    while last:
        j = last - 1
        y = pool[j]
        z = pool[last]

        if last == 1 and y >= z:
            yield ''.join(i for i in pool)
            break
        if y < z:
            pool[j] = z
            pool[last] = y
            yield ''.join(i for i in pool)
            continue

        x = pool[last - 2]

        if x >= y:
            j = last - 3
            y = pool[j]

            while y >= x:
                j = j - 1
                if j < 0:
                    break
                x = y
                y = pool[j]

            if j < 0:
                break
            if y < z:
                pool[j] = z
                pool[j + 1] = y
                pool[last] = x

                k = j + 2
                _l = last - 1

                while k < _l:
                    pool[k], pool[_l] = pool[_l], pool[k]
                    k = k + 1
                    _l = _l - 1
                yield ''.join(i for i in pool)
                continue
        else:
            if x < z:
                pool[last - 2], pool[last - 1], pool[last] = z, x, y
            else:
                pool[last - 2], pool[last - 1], pool[last] = y, z, x
            yield ''.join(i for i in pool)
            continue

        m = last - 1
        while y >= pool[m]:
            m = m - 1

        pool[j], pool[m] = pool[m], y

        pool[last], pool[j + 1] = pool[j + 1], z

        k = j + 2
        l = last - 1
        while k < l:
            pool[k], pool[l] = pool[l], pool[k]
            k = k + 1
            l = l - 1
        yield ''.join(i for i in pool)


def lexperms_reverse(_w: str) -> Generator:
    """
    less efficient but works
    a more effient one is the one the follow(elegant_lexperms_fact())
    """
    pool = sorted(list(_w))
    _n = len(pool)

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


def lexperms_reverse_fact(_x: str) -> Generator:
    """
    Lexicographic permutations in reverse order
    based on factorial counting(recursion)
    """
    pool = sorted(list(_x))
    _l = len(pool)
    _n = _l - 1

    _c = [0] * _l
    i = 1

    yield ''.join(c for c in pool)

    while _n:
        if i > _n:
            break

        if _c[i] < i:
            if i % 2 == 0 and _c[i] < 1:
                _u = 0
            else:
                _u = _c[i]

            if i == _n:
                j = 0
                while pool[j] > pool[i]:
                    j = j + 1
                _u = j

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


def elegant_next_lex(_w: str) -> Generator:
    """
    elegant
    """
    # TODO
    #     pool = sorted(list(_w))

    pool = [1, 2, 3, 4, 5]
    n = len(pool)
    l = [k + 1 for k in range(n + 1)]
    #     ind = list(range(n))
    u = list(range(n))

    l[n] = 0
    k = 1

    yield ''.join(str(c) for c in pool)
    p = 0
    q = l[0]

    while n:
        pool[k] = q

        passed = False
        j = k
        while pool[j - 1] < pool[j]:
            j = j - 1
            if j == 0:
                passed = True
                break
        if passed:
            if k == n:
                for _ in range(k):
                    k = k - 1
                    if k == 0:
                        break
                    p = u[k]
                    q = pool[k]
                    l[p] = q
            else:
                u[k] = p
                l[p] = l[q]
                k = k + 1

                p = 0
                q = l[0]
                continue
        p = q
        q = l[p]

        if q == 0:
            break


if __name__ == '__main__':
    #     w = input("Enter value to permute: ")
    #     r = test(w)
    #     print("lexco_permutations_fast\n\n", r)
    #     with open('100000.txt') as f:
    #         lines = f.readlines()
    #
    #     with open('a100000.txt') as f:
    #         answers = f.readlines()
    #
    #     t2 = time()
    #     print("LEXICO PERMUTATIONS FAST\n")
    #     for i in range(len(lines)):
    #         w = lines[i].rstrip()
    #         a = answers[i].rstrip()
    #         r = test(w)
    #         print(f'{True if r == a else {a: w}}  {"->" * 10}  {r[:85]}')
    #     elt2 = time() - t2
    #     print()
    #     print(elt2, "ELEGANT")
    #     print("lexco_permutations_fast\n")
    #     print(f"{'-' * 113}")

    T = int(input("Enter number of test cases: "))

    for _ in range(T):
        w = input("Enter value to permute: ")

        t1 = time()
        l_p = list(lexico_permutations(w))
        elt1 = time() - t1

        t2 = time()
        r = list(lexico_permutations_fast(w))
        elt2 = time() - t2

        print(f"{'-' * 113}")
        print(elt1, "NOT ELEGANT")
        print("lexco_permutations\n\n", l_p)
        print(f"{'-' * 113}")
        print(elt2, "ELEGANT")
        print("lexco_permutations_fast\n\n", r)
        print(f"{'-' * 113}")
