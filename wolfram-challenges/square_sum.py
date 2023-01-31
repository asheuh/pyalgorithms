# Problem: https://challenges.wolframcloud.com/challenge/square-sum
import sys

def square_sum(n: int):
    prev_ss = 0
    for i in range(1, n + 1):
        ss = (prev_ss + i)**2
        prev_ss = ss
    return prev_ss


if __name__ == '__main__':
    sys.set_int_max_str_digits(50000)
    n = 15
    res = square_sum(n)
    print(res)

