import sys

def solve(n, types):
    servers = {1: {'up': 0, 'down': 0}, 2: {'up': 0, 'down': 0}}
    for i in range(n):
        t = types[i]

        if t == 1:
            servers[1]['up'] += 1
        elif t == 2:
            servers[1]['down'] += 1
        else:
            if servers[1]['up'] >= servers[1]['down']:
                servers[1]['up'] += 1
            else:
                if servers[2]['up'] >= servers[2]['down']:
                    servers[2]['up'] += 1
                else:
                    servers[1]['down'] += 1
    return servers[1]['up'] + servers[2]['up']

def testig(n, types):
    ans = 0
    for i in range(n):
        k = types[i]
        if k != 2:
            ans += 1
    return ans

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for i in range(T):
        n = int(input())
        types = list(map(int, input().split()))

        r = testig(n, types)
        print(r)
