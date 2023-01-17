import sys

def solve(n):
    def length(n):
        s = 1
        while n > 10:
            n //= 10
            s += 1
        return s


    s = length(n)

    if n <= 10:
        return n

    return 9 * s

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for _ in range(T):
        n = int(input())
        r = solve(n)
        print(r)
