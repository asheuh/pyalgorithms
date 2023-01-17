import sys

def solve(n, m, w):
    for i in range(n):
        for e in w[i]:
            k = i + 1
            if k < n:
                for f in w[k]:
                    print(e, f)



if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for i in range(T):
        w = list()
        n, m = list(map(int, input().split()))

        for _ in range(n):
            ms = list(map(int, input().split()))
            w.append(ms)

        r = solve(n, m, w)
