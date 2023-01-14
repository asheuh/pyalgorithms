def dynamic_array(n, queries):
    arr = [[] * n for _ in range(n)]
    last_answer = 0
    results = []
    for query in queries:
        q, x, y = query
        idx = ((x ^ last_answer) % n)
        if q == 1:
            arr[idx].append(y)
        else:
            k = len(arr[idx])
            last_answer = arr[idx][y % k]
            results.append(last_answer)
    return results

if __name__ == '__main__':
    n = 2
    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    res = dynamic_array(n, queries)
    print(res)
