import sys

def solve(n, s):
    t = 'T'
    m = 'M'
    seq = 'TMT'

    tc = s.count(t)
    mc = s.count(m)
    k = tc - mc

    if n == 3 and k == 1:
        if s == seq:
            return 'YES'
        return 'NO'

    if n > 3:
        if k == 2:
            if tc & 1 and mc & 1:
                return 'NO'
            else:
                if tc < 5:
                    return 'YES'
                return 'NO'
        elif k == 3:
            if tc < 7:
                return 'YES'
            return 'NO'
        elif k == 1:
            return 'YES'
        else: return 'NO'
    return 'NO'

def solve2(n, s):
    pass

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    T = int(input())

    for _ in range(T):
        n = int(input())
        s = input()

        r = solve(n, s)

        print(r)

