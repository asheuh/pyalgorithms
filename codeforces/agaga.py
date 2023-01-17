import sys

def solve(n, arr):
    i = 0
    j = 1

    if len(set(arr)) == 1:
        return 'YES'

    while j < n:
        k = arr[i] ^ arr[j]

        if j >= (n - 1) and not k:
            return 'YES'

        if not k:
            i = i + 1
            j = j + 1
        else:
            arr[j] = k

        narr = arr[j:]
        l = len(narr)
        s = set(narr)

        if l >= 2 and len(s) == 1:
            return 'YES'
        
        i += 1
        j += 1

    return 'NO'


if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))

        r = solve(n, arr)
        print(r)
