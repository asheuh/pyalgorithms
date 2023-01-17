import sys

def solve(arr, n, m, x):
    pass



if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    T = int(input())

    for _ in range(T):
        n, m, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))

        r = solve(arr, n, m, x)
