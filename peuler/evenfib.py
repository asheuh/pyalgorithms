def evenfibonacci(n):
    i = 0
    j = 1
    l = [i, j]

    while 1:
        x = i + j
        i = j
        j = x

        if x > n: break
        l.append(x)

    return sum(y for y in l if y % 2)


def evenfib(n):
    limit = n
    a = 1
    b = 1
    total = 0
    fibs = []

    while b < limit:
        fibs.append(b)

        if (b % 2) == 0:
            total += b
        x = a + b
        a = b
        b = x

    return total

def evenfib2(n):
    a = 1
    b = 1
    total = 0
    c = a + b
    evens = []

    while c < n:
        total += c
        evens.append(c)
        a = b + c
        b = c + a
        c = a + b

    return total



if __name__ == '__main__':
    n = 4000000
    result = evenfib(n), evenfib2(n)
    print(result)
