def pop(x):
    count = 0
    while x != 0:
        count += 1
        x &= (x - 1)
    return count

def nlz(x):
    n = 32
    c = 16
    while c != 0:
        y = x >> c
        if y != 0:
            n -= c
            x = y
        c >>= 1
    return n - x


def ntz(x):
    x = ~x & (x - 1) # fill 1s at the position on trailing zeros e.g 01011000=>00000111
    n = 0

    while x != 0:
        n += 1
        x >>= 1
    return n

