import pprint
import string

from time import sleep


def encipher(shift: int):
    # Caesar cipher: https://en.wikipedia.org/wiki/Caesar_cipher
    alphabets = string.ascii_lowercase
    cipher = {}
    for c in range(len(alphabets)):
        x = (c + shift)
        k = 0
        if not 25 >= x >= 0:
            k = 26
        z = (x + k) % 26
        char = alphabets[z]
        if char.lower() in alphabets:
            cipher[char] = alphabets[c]
    return cipher

def decipher(encoded: str) -> str:
    for n in range(26):
        decoded = ''
        cipher = encipher(n)
        for en in encoded:
            if en in "' ,.?!":
                decoded += en
                continue
            decoded += cipher[en]
        print(decoded)
        sleep(1)

if __name__ == '__main__':
    encoded = "f'ii exsb texq peb'p exsfkd"
    decipher(encoded)

