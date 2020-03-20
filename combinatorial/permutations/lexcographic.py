from time import sleep


def lexco_permutations(x):
    """
    Lexicographic permutation generation
    
    This algorithm generates all permutations of {w1, w2 ... wn}
    visiting them in lexicographic order

    >>> w = 'brian'
    >>> result = permutations(w)
    >>> result
    >>> ['bot', 'bto', 'obt', 'otb', 'tbo', 'tob']

    Result
    ------
    The result obtained is in lexicographical order or alphabetincal order
    """
    n = len(w) - 1
    pool = list(w)

    while 1:
        j = n - 1
        yield "".join(c for c in pool)

        # Find the largest j such that pool[j] can be increased
        while pool[j] >= pool[j + 1]:
            j -= 1

        # Increase pool[j] by the smallest feasible amount
        # in this case pool[l] is the smallest element greater than
        # pool[j] that can legitimately follow pool[0] ... pool[j-1] in a permutation
        l = n
        while pool[j] >= pool[l]:
            l -= 1
        pool[j], pool[l] = pool[l], pool[j]

        # Reverse pool[j+1] ... pool[n]
        # Find the lexicographically least way to extend the new
        # pool[0]...pool[j] to a complete pattern
        k = j + 1
        c = n
        while k < l:
            pool[k], pool[c] = pool[c], pool[k]
            k = k + 1
            c = c - 1
        if j < 0:
            break


def lexco_permutations_reverse(w):
    l = len(w)
    n = l - 1
    pool = list(w)
    i = 1

    while i < n:
        while pool[i] < pool[i - 1]:
            i += 1

        j = 0
        while pool[j] > pool[i]:
            j += 1

        pool[i], pool[j] = pool[j], pool[i]

        k = i - 1
        c = 0
        while k > c:
            pool[k], pool[c] = pool[c], pool[k]
            k -= 1
            c += 1
        break
    return ''.join(c for c in pool)


def elegant_lexco_permutations(x):
    """
    Lexicographic permutations with restricted prefixes
    """
    w = str(x)
    n = len(w)
    k = 1
    L = [l for l in range(n)]
    U = [u for u in range(1, n + 1)]

    while n:
        for k in range(n):
            L[k] = k + 1
            L[n - 1] = 0
            print(L, k)


def testit(w):
    return lexco_permutations(w)


if __name__ == '__main__':
    w = input("Enter value to permute: ")
    #     elegant_lexco_permutations(w)
    #     result = lexco_permutations_reverse(w)
    #     print(result)

    result = list(testit(w))
    print(result)
