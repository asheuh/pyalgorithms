import sys
import math

from time import sleep

def gcd(n, m):
    if n <= 0:
        return m

    if n == m:
        return n

    while True:
        r = m % n
        if r == 0:
            return n

        m = n
        n = r


def power(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    p = 1

    while n:
        if n & 1:
            p *= x

        n >>= 1
        x *= x

    return p

def is_prime(n):
    if n == 1:
        return False
    if n < 4: # 2 and 3 are prime
        return True

    if n % 2 == 0: # all even numbers except 2 are not prime(2 is handled already)
        return False

    if n < 9: # we have already handled 4, 6, and 8 which are even
        return True

    if n % 3 == 0:
        return False

    r = math.floor(math.sqrt(n))
    f = 5

    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False

        f += 6
    return True

def solve():
    x = []
    y = []

    for i in range(9):
        p = power(10, i)

        while not is_prime(p):
            p += 1
        x.append(p)

        p += 1
        while not is_prime(p):
            p += 1
        y.append(p)
        
    return x, y


if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for i in range(T):
        a, b, c = [i - 1 for i in list(map(int, input().split()))] 
        x, y = solve()

        print('{} {}'.format(x[a - c] * power(10, c), y[b - c] * power(10, c)))

