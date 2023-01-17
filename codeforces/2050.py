import sys

def solve(n):
    c = 2050

    def count(num):
        counter = 1
        while num >= 10:
            num //= 10
            counter += 1
        return counter

    k = 0

    while n > 0:
        if 0 < n < c:
            k = -1
            break

        l = count(n)
        t = 2050 * 10**(l - 4)
        tl = count(t)

        if (l == tl) and n < t:
            t //= 10

        n -= t
        k += 1
        
    return k
        

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for i in range(T):
        n = int(input())
        r = solve(n)
        print(r)
