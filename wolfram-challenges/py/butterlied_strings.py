# Problem: https://challenges.wolframcloud.com/challenge/butterflied-strings


def butterflied_string(s):
    s2 = ''.join(i for i in reversed(s)) 
    return s + s2


if __name__ == '__main__':
    s = 'Wolfram'
    res = butterflied_string(s)
    print(res)
