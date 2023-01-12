def nlz(x):
    n = 32
    c = 16
    while c != 0:
        y = x >> c
        if y != 0:
            n = n - c
            x = y
        c >>= 1
    return n - x


def nlz2(x):
    # Number of leading zeros, binary search
    if x <= 0:
        return (~x >> 26) & 32
    n = 1

    if ((x >> 16) == 0):
        n = n + 16
        x = x << 16

    if ((x >> 24) == 0):
        n = n + 8
        x = x << 8

    if ((x >>28) == 0):
        n = n + 4
        x = x << 4

    if ((x >> 30) == 0):
        n = n +2
        x = x << 2

    n = n - (x >> 31)
    return n

if __name__ == '__main__':
    n = 3
    res = nlz(n)
    print(res)
