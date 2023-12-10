import sys
import math

from time import sleep


def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def first_digit(n):
    while n >= 100:
        n //= 10
    return n

def lcm(a, b):
    return b * (a // gcd(a, b))

def gcd(m, n):
    if n <= 0:
        return m

    if n == m:
        return m

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

    power = 1

    while n > 0:
        if n & 1:
            power *= x

        n >>= 1
        x *= x
    return power


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

    r = math.floor(math.sqrt(n)) # Any number n can have only one primefactor greater than square root of n
    f = 5

    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def is_coprime(m, n):
    return gcd(m, n) == 1

def i_factors(n):
    # Integer factors
    factors = []
    max_factor = math.floor(math.sqrt(n))

    for i in range(1, max_factor + 1):
        if (n % i) == 0:
            factors.extend([i, n//i])
    return set(factors)

def prime_factor(n):
    on = n
    factors = set()
    if (n % 2) == 0:
        n //= 2
        last_factor = 2

        while (n % 2) == 0:
            n //= 2
    else:
        last_factor = 1

    factors.add(last_factor)
    factor = 3
    max_factor = math.sqrt(n)

    while n > 1 and factor <= max_factor:
        if (n % factor) == 0:
            n //= factor
            last_factor = factor

            while (n % factor) == 0:
                n //= factor
            max_factor = math.sqrt(n)
            factors.add(factor)
        factor += 2

    if n == 1:
        return on, factors
    factors.add(n)
    return on, list(factors)


def my_sum(n):
    return (n * (n + 1)) // 2


if __name__ == '__main__':
    print(_factors(100))
#     input = lambda: sys.stdin.readline().rstrip()
#     print('Enter a number')
#     x = int(input())
#     print('Enter a number')
#     n = int(input())
# 
#     print(power(x, n))
#     r = first_digit(48883384893)
#     print(r)
