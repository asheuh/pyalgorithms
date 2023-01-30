# Problem: https://challenges.wolframcloud.com/challenge/maximum-roman-numeral-length

def roman_numeral(n: int):
    # generate all roman numerals up to n
    # n will be limitted to up to 5000
    roman_map {
        1: 'I', 5: 'V', 10: 'X', 50: 'L',
        100: 'C', 500: 'D', 1000: 'M': 5000: 'V̅'
    }


if __name__ == '__main__':
    n = 1000
    res = roman_numeral(n)
