def distinct_powers(n):
    results = {}
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            x = a**b
            if x not in results:
                results[x] = x
    return len(results.keys())
            


if __name__ == '__main__':
    res = distinct_powers(100)
    print(res)

