import sys

def solve(n):
    arr = [i for i in range(1, n+1)]

    if n & 1:
        arr[-1] = n - 2
        arr[-2] = n
        arr[-3] = n - 1
        n = n - 3

    for i in range(0, n, 2):
        k = i + 1
        temp = arr[i]

        if k < n:
            arr[i] = arr[k]
            arr[k] = temp

    return ' '.join([str(i) for i in arr])
        

def solve_pairs(n, arr):
    def optimized():
        maps = {}
        count = 0

        for i in range(n):
            maps[arr[i]] = i + 1 

        for i in range(1, 2 * n):
            x = i

            for j in range(1, x):
                if j * j >= x:
                    break

                if x % j == 0:
                    u = j
                    v = x // j

                    if u in maps and v in maps:
                        if (maps[u] != 0 != maps[v] and maps[u] + maps[v] == x):
                            count += 1
        return count

    def brute_force():
        count = 0
        i = 0
        j = 1

        while j < n and i < (n - 1):
            k = i + 1
            l = j + 1
            sUm = k + l

            r = arr[i] * arr[j]
            
            if sUm == r:
                count += 1
            
            j += 1

            if j == n:
                i += 1
                j = i + 1
                continue
        return count
    return optimized()


if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        r = solve_pairs(n, arr)
        print(r)
