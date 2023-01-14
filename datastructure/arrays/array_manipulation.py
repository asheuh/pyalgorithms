from itertools import accumulate


def naive_approach(n, queries):
    stack = [0 for _ in range(n)]
    for query in queries:
        a, b, k = query
        i = a - 1
        while i < b:
            stack[i] += k
            i += 1
    return max(stack)


def optimized(n, queries):
    stack = [0 for _ in range(n)]

    for query in queries:
        a, b, k = query
        i = a - 1
        stack[i] += k

        if b != n:
            stack[b] -= k
    return max(accumulate(stack))


if __name__ == '__main__':
    n = 10
    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    res = optimized(n, queries)
    print(res)
