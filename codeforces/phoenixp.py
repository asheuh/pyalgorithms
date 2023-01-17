import sys
import math

def solve(n):
    def is_sqrt(x):
        y = int(math.sqrt(x)) 
        return y * y == x

    if n & 1:
        return 'NO'
    
    if is_sqrt(n / 2):
        return 'YES'

    if (n % 4 == 0):
        if is_sqrt(n / 4):
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for _ in range(T):
        n = int(input())

        r = solve(n)
        print(r)
