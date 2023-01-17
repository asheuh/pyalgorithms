from time import sleep

def gcdSum(m):
    n = get_sum(m)

    if n == 0:
        return m

    if m == n:
        return m

    while 1:
        r = m % n
        if r == 0:
            return n

        m = n
        n = r

def get_sum(x):
    total = 0

    while x > 0:
        total += x % 10
        x //= 10
    return total

def solve2(target):
    k = target

    while 1:
        if gcdSum(k) > 1:
            return k
        k += 1

def solve(target):
    low = 0
    high = 2**31 - 1

    result = 0

    while low < high:
        mid = (low + high) >> 1
        g = gcdSum(mid)

        if mid < target:
            low = mid
        elif mid > target:
            if g > 1:
                result = mid
            high = mid
        else:
            if g > 1:
                result = mid

            if low == target:
                break
            low = mid
    return result


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        m = int(input())
        r = solve(m)
        print(r)
