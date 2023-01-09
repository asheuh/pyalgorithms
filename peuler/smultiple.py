def smallest_multiple(n):
    i = 1
    answer = None

    while 1:
        if is_divisible(i, n):
            answer = i
            break
        i += 1

    if answer:
        return answer


def is_divisible(n, r):
    for i in range(1, r + 1):
        if (n % i) != 0:
            return False
    return True


if __name__ == '__main__':
    n = 20
    result = smallest_multiple(n)
    print(result)
