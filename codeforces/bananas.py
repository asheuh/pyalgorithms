import random
import math

def find_k(ti, xi, yi, m):
    l = [i for i in range(yi + 1)]
    ai = random.choice(l)
    k = 0

    def update_k(k, xi, key):
        obj = {
                'mul': math.ceil(k * xi),
                'add': math.ceil(k + xi)
            }
        return obj[key]

    for j in range(m):
        if ti == 1:
            for j in range(ai):
                k = update_k(k, xi, 'add')
        if ti == 2:
            for j in range(ai):
                k = update_k(k, xi, 'mul')
        print(k)

def solve(ti, xi, yi, m):
    find_k(ti, xi, yi, m)


if __name__ == '__main__':
    n, m = [int(i) for i in input().split(' ')] 

    for i in range(n):
        ti, xpi, yi = input().split(' ')
        ti, xi, yi, m = int(ti), int(xpi) / 10**5, int(yi), int(m)

        r = solve(ti, xi, yi, m)

