def lexco_permutations(w):
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
    indices = [i for i in range(len(w))]

    while 1:
        j = n - 1
        a = ''.join(w[i] for i in indices)
        l = n
        yield a

        while j >= 0:
            # Find the largest j such that a[j] can be increased
            if a[j] >= a[j + 1]:
                j -= 1
                continue

            # Increase a[j] by the smallest feasible amount
            # in this case a[l] is the smallest element greater than
            # a[j] that can legitimately follow a[0] ... a[j-1] in a permutation
            if a[j] >= a[l]:
                l -= 1
                continue
            indices[j], indices[l] = indices[l], indices[j]

            # Reverse aj+1 ... a[n]
            # Find the lexicographically least way to extend the new
            # a[0]...a[j] to a complete pattern
            k = j + 1
            l = n
            while k < l:
                indices[k], indices[l] = indices[l], indices[k]
                k = k + 1
                l = l - 1
            break
        if j < 0:
            break


def elegant_lexco_permutations(w):
    """
    Lexicographic permutations with restricted prefixes
    """
    pass


def testit(w):
    perms = list(lexco_permutations(w))
    return perms


if __name__ == '__main__':
    w = input()

    result = testit(w)
    print(result)
