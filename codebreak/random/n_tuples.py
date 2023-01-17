from time import time


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
        print(s, k, x)

        j = f[0]
        f[0] = 0

        if j == n:
            break

        f[j] = f[j + 1]
        f[j + 1] = j + 1
        x[j] = 1 - x[j]

    return r


if __name__ == '__main__':
    a = [1, 7, 2, 4, 5]
    r = gray_binary_code_generation(a, 7)
    print(r)
    print()
