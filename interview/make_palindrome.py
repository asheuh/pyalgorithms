import random
import string


def make_palindrome(S):
    S_list = [s for s in S]
    letters = string.ascii_lowercase

    i = 0
    j = len(S) - 1

    while i <= j:
        fc = S[i]
        lc = S[j]
        if fc == '?' and lc != '?':
            S_list[i] = lc
        elif lc == '?' and fc != '?':
            S_list[j] = fc
        elif lc == '?' == fc:
            char = random.choice(letters)
            S_list[i] = char
            S_list[j] = char
        elif fc != lc:
            return 'NO'

        i += 1
        j -= 1
    return ''.join(S_list)


rest = make_palindrome('ba???a??a??ab')
print(rest)
