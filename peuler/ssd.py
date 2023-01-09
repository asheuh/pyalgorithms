def sum_of_square_diff(n):
    Sum = sum(i for i in range(1, n + 1))
    square_of_sum = Sum**2
    return abs(sum_of_square(n) - square_of_sum) 


def sum_of_square(n):
    total = 0

    for i in range(1, n + 1):
        s = i * i
        total += s
    return total


if __name__ == '__main__':
    n = 100
    result = sum_of_square_diff(n)
    print(result)
