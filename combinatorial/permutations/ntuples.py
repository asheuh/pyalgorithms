import pprint

from time import time, sleep
from pyalgorithms.peuler.pymath import gcd


def subsets(a):
    n = len(a)
    m = 2**n

    x = n - 1
    r = list()

    for i in range(m):
        sub = []

        for j in range(n):
            mask = i & (1 << j)
            if mask:
                sub.append(a[j])

        r.append(sub)
    return r


def mixed_radix_generation(a):
    n = len(a)
    x = [0] * n
    m = [1] * n
    subsets = []

    while n:
        j = n - 1

        while x[j] == m[j]:
            x[j] = 0
            j -= 1

        if j < 0:
            break

        x[j] = x[j] + 1
        sub = [a[k] for k in range(len(x)) if x[k]]
        subsets.append(sub)
    return subsets


def gray_subset_generation(a):
    l = len(a)
    n = l - 1
    x = [0] * n
    f = [j for j in range(l)]

    r = list()

    while n:
        m = [0] + x
        m1 = [1] + x
        j = f[0]
        f[0] = 0

        if j >= n:
            break

        x, f = swap(x, f, j)
        
        # Find the subset
        s = [a[i] for i in range(l) if m[i]]
        k = [a[0]] + s
        r.append(s)
        r.append(k)
    return r

def gray_find_total_power(a):
    l = len(a)
    n = l - 1
    x = [0] * n
    f = [j for j in range(l)]
    modulo = (10**9 + 7)
    p = a[0]
    total_power = p * p

    while n:
        j = f[0]
        f[0] = 0
        if j >= n:
            break

        x, f = swap(x, f, j)
        
        # Find the subarray
        v = ''.join(str(c) for c in x)
        h = int(v, 2)
        h //= (((h ^ (h - 1)) >> 1) + 1) # remove trailing clear bits
        if not ((h + 1) & h): # check if all bits are set bits
            m = [0] + x
            s = []
            k = [a[0]]
            stop = False
            for i in range(1, l):
                if m[i]:
                    s.append(a[i])
                if i == 1 and not m[i]:
                    k = []
                    stop = True
                if not stop and m[i]:
                    k.append(a[i])
            if s:
                total_power += min(s) * sum(s)
            if k:
                total_power += min(k) * sum(k)
    return total_power

def swap(x, f, j):
    f[j] = f[j + 1]
    f[j + 1] = j + 1
    x[j] = 1 - x[j]
    return x, f


def gray_binary_code_generation(a):
    n = len(a)
    k = n - 1
    x = [0] * k
    f = [i for i in range(n)]

    while k:
        m = [0] + x
        m1 = [1] + x
        print(int(''.join(str(c) for c in m), 2))
        print(int(''.join(str(c) for c in m1), 2))
        sleep(0.3)
        j = f[0]
        f[0] = 0

        if j >= k:
            break

        x, f = swap(x, f, j)


def find_next(x):
    """
    Finding the next higher number after a given number that has
    the same number of set bits(1-bits)
    """
    def ntz(s):
        lookup = [
            32, 0, 1, 26, 2, 23, 27, 0,
            3, 16, 24, 30, 28, 11, 0, 13,
            4, 7, 17, 0, 25, 22, 31, 15,
            29, 10, 12, 6, 0, 21, 14, 9,
            5, 20, 8, 19, 18
        ]
        return lookup[s % 37]

    smallest = x & -x # Isolate learst significant bit
    # turn the clear just before all the rightmost contiguous set bits in x
    # e.g x = 0111 then ripple = 1000
    ripple = x + smallest 
    ones = x ^ ripple
    ones >>= (2 + ntz(smallest)) # ntz(x): Number of trailling zeros in x or (ones >> 2) // smallest
    return ripple | ones

def subsets_bits(x):
    n = len(x)
    m = 2**n
    mapsubsets = {}
    
    for i in range(1, m):
        if i not in mapsubsets:
            mapsubsets[i] = find_next(i)
    return mapsubsets


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
    nex = subsets_bits(a)
    print(nex)
    # r = gray_binary_code_generation(a)
    # pprint.pprint(r)
