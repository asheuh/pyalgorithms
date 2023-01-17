import sys

def solve(ws, n, x):
    ws.sort()
    weight = 0
    i = n - 1
    k = i - 1
    maps = {}

    while i >= 0:
        weight += ws[i]
        
        if weight == x:
            k = i - 1
            if k >= 0:
                weight -= ws[i]
                weight += ws[k]

            ws[i], ws[k] = ws[k], ws[i]
        
        maps[ws[i]] = ws[i]

        i -= 1
        k -= 1

    if weight == x:
        print('NO')
    else:
        print('YES')
        print(' '.join([str(i) for i in maps.keys()]))

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    T = int(input())

    for i in range(T):
        n, x = list(map(int, input().split()))
        ws = list(map(int, input().split()))

        solve(ws, n, x)
