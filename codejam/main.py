import random
from itertools import permutations

def reversort(arr):
    """Using swapping"""
    n = len(arr)
    result = 0

    for i in range(n):
        j = i
        k = i
        smallest = arr[k]

        while k < n:
            if arr[k] < smallest:
                smallest = arr[k]
                j = k
            k += 1

        v = arr[i]
        r = arr[j]

        if v > r:
            arr[i] = r
            arr[j] = v
            result += j - i + 1

    return arr, result + 1

def reversort2(L):
    """Using reverse"""

    n = len(L)
    result = 0
    arr = L[::]
    
    for i in range(n):
        j = i
        k = i

        smallest = arr[k]
        
        while k < n:
            if arr[k] < smallest:
                smallest = arr[k]
                j = k
            k += 1
        
        jth = j
        ith = i

        while ith < jth:
            arr[ith], arr[jth] = arr[jth], arr[ith]
            jth -= 1
            ith += 1

        result += j - i + 1

    return result - 1

def find_list(N, C):
    arr = list(range(1, N + 1))
    perms = permutations(arr)

    results = []

    for perm in [list(item) for item in perms]:
        cost = reversort2(perm)

        if cost == C:
            results.append(perm)

    if not results:
        return 'IMPOSSIBLE'
    return random.choice(results)


def moons_umbrellas(x, y, s):
    keys = ['C', 'J']
    costs = {'CJ': x, 'JC': y}
    n = len(s)

    def counter(s, x, y):
        counts = {'CJ': x, 'JC': y}
        n = len(s)
        cost = 0
        prev = 0
        current = 1

        if isinstance(s, list):
            s = ''.join(s)

        while current < n:
            f = s[prev:current + 1]
            if f in counts:
                cost += counts[f]

            current += 1
            prev += 1
        return cost

    if '?' not in s:
        return counter(s, x, y)

    s = [c for c in s]

    i = 0
    while i < n:
        if i == 0 and s[i] == '?':
            k = i
            while k < n and s[k] == '?':
                k += 1
            if k >= n:
                s[:k] = ['C'] * k
                i = k
                continue

            if s[k] == 'J':
                s[:k] = ['J'] * k
            else:
                s[:k] = ['C'] * k
            i = k
        elif s[i] == '?':
            p = i - 1
            k = i
            while k < n and s[k] == '?':
                k += 1
            if k >= n:
                if s[p] == 'J':
                    s[p:k] = ['J'] * (k - p)
                else:
                    s[p:k] = ['C'] * (k - p)
                i = k
            else:
                c = s[p]
                h = s[k]
                if c == h:
                    s[p:k] = [c] * (k - p)
                else:
                    if c == 'C':
                        s[p:k] = [c] * (k - p)
                    else:
                        s[p:k] = [c] * (k - p)
        i += 1
    return counter(s, x, y)

if __name__ == '__main__':

    from time import time
    arr = [4, 2, 3, 10, 12, 11, 8, 9, 7, 5, 6, 1]
    arr2 = [7, 6, 5, 4, 3, 2, 1]
    arr3 = [4, 2, 1, 3]
    revsort2 = reversort2(arr3)
    revsort = reversort(arr2)
    mu = moons_umbrellas(50, 100, '???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')

    t = time()
    parr = find_list(4, 6)
    e = time() - t
    print(revsort)

