"""
imports
"""
from typing import Generator
from time import sleep, time


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
    pool = sorted(list(_x))

    yield "".join(c for c in pool)

    while 1:
        j = _n - 1

        # Find the largest j such that pool[j] can be increased
        while pool[j] > pool[j + 1]:
            j -= 1

        # Increase pool[j] by the smallest feasible amount
        # in this case pool[l] is the smallest element greater than
        # pool[j] that can legitimately follow pool[0] ... pool[j-1] in a permutation
        _l = _n
        while pool[j] > pool[_l]:
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


def elegant_next_lex(_w: str) -> Generator:
    """
    elegant
    """
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
        if k < n:
            pool[k] = q

        print(p, q, k, pool)
        sleep(.4)

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


def elegant_lexperms_fact(_x: str) -> Generator:
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


if __name__ == '__main__':
    #     T = int(input("Enter number of test cases: "))
    #     w = input("Enter value to permute: ")
    e_n_l = list(elegant_next_lex(''))
    print(e_n_l)

#     for _ in range(T):
#         w = input("Enter value to permute: ")
#         t1 = time()
#         r_e_f = list(elegant_lexperms_fact(w))
#         elt1 = time() - t1

#         t2 = time()
#         r_l_r = list(lexperms_reverse(w))
#         elt2 = time() - t2

#         l_p = list(lexco_permutations(w))
#         e_n_l = list(elegant_next_lex(w))
#         print(f"{'-' * 113}")
#         print(e_n_l)
#         print(elt1, "ELEGANT")
#         print(r_e_f)
#         pprint(int(sum(int(n) for n in r_e_f) / len(r_e_f)))
#         print(f"{'-' * 113}")
#         print(elt2, "NOT ELEGANT")
#         print(r_l_r)
#         print(f"{'-' * 113}")
#         print("lexperms_reverse", r_l_r)
#         print(f"{'-' * 113}")
#         print("lexco_permutations", l_p)
#         print(f"{'-' * 113}")
