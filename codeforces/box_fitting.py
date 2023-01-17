import sys
import math

def solve(n, W, ws):
    ws.sort(reverse=True)
    h = 1
    curr = W
    box = []

    counts = [0 for _ in range(10)]

    for w in ws:
        counts[int(math.log(w, 2))] += 1

    while n > 0:
        pass



if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    T = int(input())

    for _ in range(T):
        n, W = list(map(int, input().split()))
        ws = list(map(int, input().split()))
        r = solve(n, W, ws)
