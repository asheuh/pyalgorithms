def ntz(x):
    x = ~x & (x - 1) # fill 1s at the position on trailing zeros e.g 01011000=>00000111
    n = 0

    while x != 0:
        n += 1
        x >>= 1
    return n

def ntz1(x):
    # Reiser's algorithm
    lookup = [
        32, 0, 1,  26, 2,  23, 27, 0,  3,  16, 24, 30, 28,
        11, 0, 13, 4,  7,  17, 0,  25, 22, 31, 15, 29, 10,
        12, 6, 0,  21, 14, 9,  5,  20, 8,  19, 18
    ]
    x = (x & -x) % 37
    return lookup[x]


def ntz2(x):
    # Using a de Bruijn cycle algorithm
    lookup = [
        0, 1, 2, 24, 3, 19, 6, 25,
        22, 4, 20, 10, 16, 7, 12, 24,
        31, 23, 18, 5, 21, 9, 15, 11,
        30, 17, 8, 14, 29, 13, 28, 27
    ]
    if x == 0:
        return 32
    x = (x & -x) * 0x04D7651F
    return lookup[x >> 27]


if __name__ == '__main__':
    n = 8
    res = ntz1(n)
    print(res)
