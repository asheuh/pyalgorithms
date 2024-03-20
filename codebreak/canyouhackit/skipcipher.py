from pyalgorithms.peuler.pymath import is_coprime


def skip_cipher(cipher):
    n = len(cipher)

    for m in range(1, 10):
        if not is_coprime(m, n):
            continue

        array = [''] * n
        for i in range(1, n + 1):
            char = cipher[i-1]
            index = (i - 1) * m % n
            array[index] = char

        message = ''.join(array)
        print(m, '========>', message)


if __name__ == '__main__':
    cipher = 'K riso  reso.purdl,tunelreofnceuoeiceey e sby m s'
    plain_text = skip_cipher(cipher)
