def number_triangles(n: int):
    results = []
    for i in range(1, n + 1):
        results.append(tuple(range(1, i + 1)))
    return results


if __name__ == '__main__':
    res = number_triangles(8)
    print(res)
