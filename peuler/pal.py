from time import time
from itertools import combinations

def pal(start, end):
    l = [i for i in range(start, end)]
    r = combinations(l, 2)
    pals = []

    for combination in r:
        a, b = combination
        number = a * b
        reverse = ''.join(i for i in reversed(str(number)))

        if reverse == str(number):
            pals.append(number)
    
    return max(pals)


def reverse(n):
    reverse = 0
    while n > 0:
        remainder = n % 10
        reverse = (10 * reverse) + remainder
        n //= 10
    return reverse

def is_palindrome(n):
    return n == reverse(n)


def largest_palindrome(start, end):
    largest_palindrome = 0
    a = start
    # assuming end is 1 greater than the number that is 
    # less than end and has len if 1 less end e.g end = 1000, then end = 1000 - 1 = 999
    end = end - 1

    while a <= end:
        b = start

        while b <= end:
            k = a * b

            if is_palindrome(k) and k > largest_palindrome:
                largest_palindrome = k
            b += 1
        a += 1
    return largest_palindrome

def largest_palindrome_fast(start, end):
    largest_palindrome = 0
    a = start
    # assuming end is 1 greater than the number that is 
    # less than end and has len if 1 less end e.g end = 1000, then end = 1000 - 1 = 999
    end = end - 1

    while a <= end:
        b = a

        while b <= end:
            k = a * b

            if is_palindrome(k) and k > largest_palindrome:
                largest_palindrome = k
            b += 1
        a += 1
    return largest_palindrome

def largest_palindrome_faster(start, end):
    x = end - 1
    largest_palindrome = 0
    a = x

    while a >= start:
        b = x
        while b >= a:
            k = a * b
            if k <= largest_palindrome:
                break # Since k a * b is always going to be too small

            if is_palindrome(k):
                largest_palindrome = k
            b -= 1
        a -= 1
    return largest_palindrome

def largest_palindrome_fastest(start, end):
    largest_palindrome = 0
    a = end - 1
    while a >= start:
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990
            db = 11

        while b >= a:
            if a * b <= largest_palindrome:
                break
            if is_palindrome(a * b):
                largest_palindrome = a * b

            b = b - db
        a = a - 1
    return largest_palindrome

if __name__ == '__main__':
    end = 1000
    start = 100
    t1 = time()
    r = largest_palindrome_fast(start, end)
    e1 = time() - t1

    t2 = time()
    r1 = largest_palindrome(start, end)
    e2 = time() - t2

    t3 = time()
    r2 = pal(start, end)
    e3 = time() - t3

    t4 = time()
    r3 = largest_palindrome_faster(start, end)
    e4 = time() - t4

    t5 = time()
    r4 = largest_palindrome_fastest(start, end)
    e5 = time() - t5

    print(e1, e2, e3, e4, e5)
    print(r, r1, r2, r3, r4)
