import math

from pymath import is_prime

from time import sleep


def summation_primes(n):
    total = 2
    for i in range(3, n, 2):
        if is_prime(i):
            total += i
    return total

def eratosthenes(n):
    pass


if __name__ == '__main__':
    n = 30
    res = eratosthenes(n)
    print(res)
