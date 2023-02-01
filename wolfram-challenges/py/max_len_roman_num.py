# Problem: https://challenges.wolframcloud.com/challenge/maximum-roman-numeral-length
import math

def roman_numeral(n: int):
    # generate all roman numerals up to n
    # n will be limitted to up to 5000
    values = [
        5000, 4000, 1000,
        900, 500, 400, 100,
        90, 50, 40, 10, 9,
        5, 4, 1
    ] 
    romans = [
        'V̅', 'I̅V̅', 'M',
        'CM', 'D', 'CD',
        'C', 'XC', 'L',
        'XL', 'X', 'IX',
        'V', 'IV', 'I'
    ]

    result = ''
    i = 0
    while n:
        while n >= values[i]:
            n -= values[i]
            result += romans[i]
        i += 1
    return result

def max_len(n: int):
    # Maximum Roman Numeral Length
    max_l = -math.inf

    for i in range(1, n + 1):
        rn = roman_numeral(i)
        l = len(rn)
        
        if l > max_l:
            max_l = l
    return max_l


if __name__ == '__main__':
    n = 5000
    res = max_len(n)
    print(res)
