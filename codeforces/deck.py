import sys

def solve(n, q, cards, q_c):
    stack = []
    pos = [-1] * 55

    for i in range(n):
        if pos[cards[i]] == -1:
            pos[cards[i]] = i + 1

    for q in q_c:
        stack.append(pos[q])

        i = 0
        while i < len(pos):
            print(pos)
            p = pos[i]
            if p < pos[q]:
                pos[i] += 1
            i += 1
        pos[q] = 1
    return stack
        


if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    n, q = list(map(int, input().split()))
    c = list(map(int, input().split()))
    q_c = list(map(int, input().split()))

    r = solve(n, q, c, q_c)
    print(' '.join([str(num) for num in r]))

