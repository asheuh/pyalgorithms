import re
import math
import pprint

from string import ascii_lowercase, punctuation

def parse_string(key, remove_dup):
    if remove_dup:
        newkey = ''
        _keys = {}
        for c in key:
            if c in _keys:
                continue
            newkey += c
            _keys[c] = True
        key = newkey
    return key.replace(' ', '').translate(str.maketrans('', '', punctuation))

def transposecipher(fkey: str, skey: str, message: str, remove_dup: bool=True):
    keys = [fkey, skey]
    message = parse_string(message, False)
    for key in keys:
        key = parse_string(key, remove_dup) # memory word
        ascii_map = [a.upper() for a in sorted(key)]

        n = len(key)
        grid = []
        while message:
            block = message[:n]
            message = message[n:]
            if len(block) != n:
                block += '*' * (n - len(block)) # Padding
            grid.append(block)

        transposed = [''.join(l) for l in zip(*grid)]
        unparsedcipher = {}
        indices = {}
        for i, c in enumerate(key):
            char = c.upper()
            index = ascii_map.index(char)
            if index in indices:
                index += 1

            unparsedcipher[index + 1] = transposed[i].replace('*', ' ') 
            indices[index] = True

        mcipher = ''
        for rank in sorted(unparsedcipher.keys()):
            mcipher += unparsedcipher[rank]

        message = mcipher
    return message.upper()

def parse_blocks(cipher, size):
    result = ''
    while cipher:
        result += cipher[:size]
        result += ' '
        cipher = cipher[size:]
    return result


def decrypt(cipher, keys):
    _cipher = parse_string(cipher, False)
    n = len(_cipher)

    for key in keys:
        key = parse_string(key, True)
        key_map = list(sorted(key))
        row = len(key)
        col = math.ceil(n / row)
        grid = {}
        rank = 1
        tcipher = cipher

        while tcipher:
            block = tcipher[:col]
            tcipher = tcipher[col:]
            grid[rank] = block
            rank += 1

        indices = {}
        dec_cipher = []
        for c in key:
            index = key_map.index(c) + 1
            if index in indices:
                index += 1

            dec_cipher.append(grid[index])

        message = ''
        for text in zip(*dec_cipher):
            message += ''.join(text)

        cipher = message
    return cipher


if __name__ == '__main__':
    fkey = 'cryptographic'
    skey = 'network security'
    message = 'Be at the third pillar from the left outside the lyceum theatre tonight at seven. If you are distrustful bring two friends.'
    cipher = transposecipher(fkey, skey, message)
    print('ENCRYPTED:')
    print(cipher)
    print()
    message = decrypt(cipher, [skey, fkey])
    print('DECRYPTED:')
    print(message)
