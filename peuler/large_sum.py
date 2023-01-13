def large_sum(digits):
    total = 1
    for digit in digits:
        total += digit

    n = len(str(total)) - 10
    while n:
        total //= 10
        n -= 1
    return total


if __name__ == '__main__':
    data = [int(i) for i in open('large_sum_input.txt').read().rstrip().split('\n')]
    res = large_sum(data)
    print(res)
