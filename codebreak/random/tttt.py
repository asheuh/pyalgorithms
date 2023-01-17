def counting_sort(arr):
    """Efficient when sorting values in a small range
    for example: 1-100, 1-1000 etc.
    """
    mn = min(arr)
    mx = max(arr)
    seen = {}
    result = []

    for i in arr:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1

    for v in range(mn, mx + 1):
        c = seen.get(v, 0)
        result.extend([v] * c)

    print(result)

counting_sort([3,1,2,1,4,5,6,1,2,3,6,6,6])

