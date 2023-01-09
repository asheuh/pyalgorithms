def t(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            print(l[i], l[j], (i, j))


def T(l):
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            print(i, j, l)


l = [11,33,53,2,45,63,5]
T(l)
