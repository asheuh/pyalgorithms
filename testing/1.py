#!/bin/python3


def organizingContainers(container):
    n = len(container)

    total = 0

    for c in container:
        total += sum(c)

    i = 0

    while n:
        index = (i + 1) % n

        c = container[i]
        cn = container[index]

        print(c, i)

        if c[index] > 0 and cn[i] > 0:
            c[i] += 1
            c[index] -= 1
            cn[i] -= 1
            cn[index] += 1
        else:
            index = index + 1
            if index != n:
                continue

        i += 1
        total -= 1

        if i == n:
            i = 0

        if total == 0:
            break


if __name__ == '__main__':
    q = int(input('Enter an integer: '))

    for q_itr in range(q):
        n = int(input('Enter an integer: '))

        container = []

        for _ in range(n):
            container.append(
                list(
                    map(
                        int,
                        input(f'Enter {n} space separated digits: ').rstrip().
                        split())))

        organizingContainers(container)
