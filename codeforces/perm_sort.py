import sys


def solve(perm, n):
    print(perm, n)


if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for _ in range(T):
        n = int(input())
        perm = list(map(int, input().split()))

        r = solve(perm, n)

