def fizzbuzz(n):
    results = []

    for i in range(1, n + 1): # Multiple of 3
        k = i
        if i % 3 == 0:
            k = 'fizz'
        elif i % 5 == 0: # Multiple if 5
            k = 'buzz'
        elif (i % 5) == 0 == (i % 3): # Multiple of both 3 and 5
            k = 'fizzbuzz'
        results.append(k)
    return results


if __name__ == '__main__':
    n = 1000
    res = fizzbuzz(n)
    print(res)
