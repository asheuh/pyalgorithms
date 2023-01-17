import sys
import random
from time import sleep

def solve(N, m):
    a = [i for i in range(10)]
    count = 0

    def first_digit(k):
        while k >= 10:
            k = k / 10
        return k

    for i in range(N):
        ki = m[i]
        f = str(ki) 
        k = first_digit(ki)
            
        c = len(f[1:])
        j = i + 1
    
        if j < N:
            li = m[j]

            if li < 1:
                break

            s = str(li)
            l = first_digit(li)

            if k > l:
                while ki >= li: 
                    ci = 0
                    for _ in range(c):
                        h = random.choice(a)
                        s += str(h)
                        li = int(s)
                        ci += 1
                        if ki < li:
                            break
                    count += ci
                m[j] = li
            else:
                while ki >= li:
                    ci = 0
                    if c > 0:
                        for _ in range(c):
                            h = random.choice(a)
                            s += str(h)
                            li = int(s)
                            ci += 1
                            if ki < li:
                                break
                    else:
                        h = random.choice(a)
                        s += str(h)
                        li = int(s)
                        ci += 1
                    count += ci
                m[j] = li
    return count



if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for i in range(T):
        N = int(input())
        m = list(map(int, input().split()))

        r = solve(N, m)
        print('Case #{}: {}'.format(i + 1, r))
