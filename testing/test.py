from time import sleep, time


def binary_search(a, k):
    n = len(a) - 1
    l = 0
    u = n
    if n == 0:
        return 0

    while n:
        i = (l + u) >> 1

        if u < l:
            index = i
            break

        if k > a[i]:
            u = i - 1
        elif k < a[i]:
            l = i + 1
        else:
            index = i
            break
    return index


def leaderboard(s, a):
    sl = len(s)
    al = len(a)

    ranks = dict()

    i = 0
    r = 1

    while i < sl:
        ranks[s[i]] = r
        n = i + 1

        if n == sl:
            break

        x = s[i]
        y = s[n]

        if x != y:
            r = r + 1
        i = i + 1

    for ascore in a:
        index = binary_search(s, ascore)
        if s[index] == ascore:
            rank = ranks[s[index]]
        else:
            rank = ranks[s[index]] + 1
        if index < 0:
            rank = 1
        print(rank)


def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i
    return fact


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
    m = [2] * n

    while n:
        j = n - 1

        while x[j] == m[j] - 1:
            x[j] = 0
            j = j - 1

        if j < 0:
            break

        x[j] = x[j] + 1


def gray_binary_code_generation(a, p):
    l = len(a)
    n = l - 1
    x = [0] * n
    f = [j for j in range(l)]

    r = list()

    while n:
        m = [0] + x
        s = [a[i] for i in range(l) if m[i] == 1]

        k = [a[0]] + s

        r.append(s)
        r.append(k)

        j = f[0]
        f[0] = 0

        if j == n:
            break

        f[j] = f[j + 1]
        f[j + 1] = j + 1

        x[j] = 1 - x[j]


#     rn = list()
#
#     for i in r:
#         j = 0
#         y = len(i)
#         if y == l:
#             continue
#
#         if y > 1:
#             A = i[j]
#             B = i[j + 1]
#             if (A % p) + (B % p) == p:
#                 rn.append(y)
    return r


def test(a, k):
    n = len(a)

    counts = [0] * k

    for i in range(n):
        counts[a[i] % k] += 1

    count = min(counts[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += max(counts[i], counts[k - i])
    if k % 2 == 0:
        count += 1


def queensAttack(n, k, r_q, c_q, obstacles):

    if (r_q == n or r_q == 0) and (k == 0):
        return (n - 1) * 3

    count = 0
    obs = {}

    dir_coords = {
        "ne": (-1, 1),
        "nw": (1, 1),
        "se": (-1, -1),
        "sw": (1, -1),
    }

    for o in obstacles:
        if o[0] == r_q:
            if o[1] > c_q:
                r = o[1] - c_q
            else:
                r = c_q - o[1]
            count += (r - 1)
        if o[1] == c_q:
            if o[0] > r_q:
                c = o[0] - r_q
            else:
                c = r_q - o[0]
            count += (c - 1)
        obs[str(o)] = None

    for coord in dir_coords:
        a, b = dir_coords[coord]
        x = r_q
        y = c_q

        while n:
            x += a
            y += b
            count += 1

            if str([x, y]) in obs:
                break
            if y > n or x < 1 or y < 1 or x > n:
                break
        count = count - 1

    return count


def queensattack(n, k, r_q, c_q, obstacles):

    if (r_q == n or r_q == 0) and (k == 0):
        return (n - 1) * 3

    obs = {}

    dir_coords = {
        "n": (0, 1),
        "e": (-1, 0),
        "w": (1, 0),
        "ne": (-1, 1),
        "nw": (1, 1),
        "s": (0, -1),
        "se": (-1, -1),
        "sw": (1, -1),
    }

    for o in obstacles:
        obs[str(o)] = None

    count = 0

    for coord in dir_coords:
        a, b = dir_coords[coord]
        x = r_q
        y = c_q

        while n:
            x += a
            y += b
            count += 1

            if str([x, y]) in obs:
                break
            if y > n or x < 1 or y < 1 or x > n:
                break
        count = count - 1
    return count


if __name__ == '__main__':
    #     s = [100, 100, 50, 40, 40, 20, 10]
    #     s1 = [1]
    #     a1 = [1, 1]
    #     a = [5, 25, 50, 120]
    #     leaderboard(s1, a1)
    #     r = factorial(-2)
    #     a = [
    #         278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575,
    #         436
    #     ]
    #     a = [1, 7, 2, 4, 5]
    #     a = [1, 7, 2, 6]
    #     test(a, 3)
    #     s1 = time()
    #     rs = subsets(a)
    #     e = time() - s1
    #     print(rs)
    #     print()
    #     print('Algorithm 1: ', e)
    #
    #     s2 = time()
    #     r = gray_binary_code_generation(a, 7)
    #     e1 = time() - s2
    #     print(r)
    #     print()
    #     print('Algorithm 2: ', e1)
    #     nk = input('Enter 2 integer separated by space: ').split()
    n = 100000
    k = 100000
    #     rqcq = input('Enter 2 integer separated by space: ').split()
    #     print()
    rq = 8703
    cq = 2054

    with open('sss.csv') as f:
        lines = f.readlines()
    obstacles = list()

    for line in lines:
        l = list(map(int, line.rstrip('\n').split()))
        obstacles.append(l)

    s1 = time()
    result = queensAttack(n, k, rq, cq, obstacles)
    e1 = time() - s1

    s2 = time()
    r = queensattack(n, k, rq, cq, obstacles)
    e2 = time() - s2
    print(result, r, e1, e2)
