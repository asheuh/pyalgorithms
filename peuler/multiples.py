from time import time

def multiples(n):
    total = 0

    for i in range(1, n):
        if not (i % 5) or not (i % 3):
            total += i
    return total

def multiples_efficient(n):
    return sum_divisible_by(n, 3) + sum_divisible_by(n, 5) - sum_divisible_by(n, 15)

def sum_divisible_by(n, r):
    """Pretty fast"""
    target = n - 1

    p = target // r
    return r * (p * (p + 1)) // 2



if __name__ == '__main__':
    n = 1000000000
#     t1 = time()
#     result = multiples(n)
#     e1 = time() - t1

    t2 = time()
    r = multiples_efficient(n)
    e2 = time() - t2
    print(r, e2)
    
