import pprint

from time import sleep


def number_letter_count(n):
    upto_twenty = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
        100: 'onehundred'
    }
    stack = []
    i = 1
    last = None
    total = 0
    while i <= n:
        word = upto_twenty.get(i)
        if not word:
            last = stack[-1]
            k = i
            x = str(last[0])
            if len(x) == 2:
                i = 1
                while i < 10:
                    lword = upto_twenty[i]
                    y = str(i)
                    d = int(x[0] + y)
                    w = last[1] + lword
                    stack.append((d, w))
                    upto_twenty[d] = w 
                    print('word', w)
                    total += len(w)
                    i += 1
                i = (i - 2) + k
        else:
            total += len(word)
            print('word', word)
            stack.append((i, word))
        i += 1

    x = 'hundred'
    stack.pop()

    for i in range(1, 10):
        v = upto_twenty[i]
        ihundred = v + x
        y = len(ihundred)
        if ihundred == 'onehundred':
            y = 0
        total += y
        for num, item in stack:
            word = v + x
            word2 = 'and' + item
            c = len(word + word2)
            total += c

    return total + len('onethousand')


if __name__ == '__main__':
    n = 1000
    res = number_letter_count(n)
    print(res)
