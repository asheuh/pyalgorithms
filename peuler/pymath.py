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


if __name__ == '__main__':
    print(is_prime(4533973694165307953397369416530795339736941653079533973694165307953973694165307953))
#     input = lambda: sys.stdin.readline().rstrip()
#     print('Enter a number')
#     x = int(input())
#     print('Enter a number')
#     n = int(input())
# 
#     print(power(x, n))
#     r = first_digit(48883384893)
#     print(r)
