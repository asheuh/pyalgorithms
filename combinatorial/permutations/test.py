def lexperms(w):
    pool = list(w)
    l = len(pool)
    n = l - 1

    if n < 3:
        return ''.join(i for i in pool)

    while n:
        j = n - 1
        y = pool[j]
        z = pool[n]

        if y < z:
            pool[j] = z
            pool[n] = y

        return pool


r = lexperms('ab')
print(r)
