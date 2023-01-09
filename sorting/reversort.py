def reversort(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        # j is the position with the minimum value in arr between i and length(arr), inclusive
        j = arr.index(min(arr[i:]), i, n)

        c = j
        k = i
        # Reverses the sublist going from the i-th position to the current position of the i-th minimum element
        while k < c:
            arr[k], arr[c] = arr[c], arr[k]
            c -= 1
            k += 1
        result += j - i + 1
    return result - 1, arr

def sum_digits(n):
    t = 0
    while n > 0:
        t += n % 10
        n /= 10
    return t

def first_digit(n):
    while n >= 10:
        n //= 10
    return n

if __name__ == '__main__':
    a = [11,33,53,2,45,63,5,6,3,9,4,100,102,101,32,23,20,21]
    r = reversort(a)
    res = first_digit(812453)
    print(res, r)
