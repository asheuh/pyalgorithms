# Problem: https://challenges.wolframcloud.com/challenge/multiples-of-3-and-5


def three_five(n: int):
    count = 0
    for i in range(1, n + 1):
        if (i % 5) == 0 == (i % 3):
            count += 1
    return count


if __name__ == '__main__':
    n = 123456
    res = three_five(n)
    print(res)
