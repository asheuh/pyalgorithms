import sys

from time import sleep


def solve(n, arr):
    i = 0
    j = 1
    count = 0
    stack = []
    k = (arr[i], arr[j])

    while j < n:
        r = sum(k) % 2
        
        if j == (n - 1):
            return arr

        if not r:
            f = j + 1
            if f < n:
                if not (k[1] + arr[f]) % 2:
                    for e in k:
                        stack.append(e)
                    i = j
                    j = f
                else:
                    stack.append(k[0])
        else: 
            f = j + 1
            if f < n:
                a = arr.pop(j)
                arr.append(a)
                count += 1

                k = (arr[i], arr[j])

            if (j + count) >= n:
                return arr
            continue
        
        if ((n - 1) - j == count):
            return arr

        i += 1
        j += 1

        if j < n:
            k = (arr[i], arr[j])

    return stack

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        r = solve(n, arr)
        print(' '.join([str(item) for item in r]))
