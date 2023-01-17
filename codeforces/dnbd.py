import sys

def solve(n, s):
    
    i = 0
    j = 1
    seen = {}
    result = 'YES'
    finished = 0

    while i < n:
        current = s[i]

        if current in seen and seen[current] == finished:
            # this means the tasks is being revisited which makes it suspicious
            result = 'NO'
            break
        
        if j < n:
            if current == s[j]:
                seen[current] = 1

                while current == s[j]:
                    seen[current] += 1
                    j += 1
                    if j >= n:
                        break

                i = j - 1
                continue
            else:
                seen[current] = finished 

        j += 1
        i += 1
    return result


if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()

    T = int(input())

    for _ in range(T):
        n = int(input())
        s = input()
        r = solve(n, s)
        print(r)
