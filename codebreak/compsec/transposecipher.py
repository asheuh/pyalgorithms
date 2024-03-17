import re
import pprint

from string import ascii_lowercase, punctuation

def transposecipher(fkey: str, skey: str, message: str, remove_dup: bool, encrypt: bool=True):
    keys = [fkey, skey]

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

            unparsedcipher[index + 1] = transposed[i].replace('*', '') 
            indices[index] = True

        mcipher = ''
        for rank in sorted(unparsedcipher.keys()):
            mcipher += unparsedcipher[rank]

        message = mcipher
    return parse_blocks(message.upper(), 5) 

def parse_blocks(cipher, size):
    result = ''
    while cipher:
        result += cipher[:size]
        result += ' '
        cipher = cipher[size:]
    return result


if __name__ == '__main__':
    fkey = 'cryptographic'
    skey = 'network security'
    message = 'Be at the third pillar from the left outside the lyceum theatre tonight at seven. If you are distrustful bring two friends.'
    cipher = transposecipher(fkey, skey, message, True)
    print(cipher)
