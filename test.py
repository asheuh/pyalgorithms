def _max(a):
    n = len(a)

    # two instructions (one for looking up the value a[0] and for assigning the value to m)
    m = a[0]

    for i in range(n):
        if a[i] >= m:
            m = a[i]

    return m


if __name__ == '__main__':
    a = [
        12, 42, 5, 4, 3, 7, 89, 8, 65, 34, 56, 245, 64, 4545, 34, 23, 4, 25, 6,
        46
    ]
    r = _max(a)
    print(r)
