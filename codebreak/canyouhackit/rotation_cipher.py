import pprint
import string

from time import sleep


def encipher(plain_text: str, shift: int):
    # Caesar cipher: https://en.wikipedia.org/wiki/Caesar_cipher
    n = len(plain_text)
    cipher = ''
    for char in plain_text:
        if char.isalpha():
            k = 97
            if char.isupper():
                k = 65
            _char = chr((ord(char) + shift - k) % 26 + k)
            cipher += _char
        else:
            cipher += char
    return cipher

def decipher(cipher: str, shift: int):
    plain_text = ''
    for char in cipher:
        if char.isalpha():
            k = 97
            if char.isupper():
                k = 65
            _char = chr((ord(char) - shift - k) % 26 + k)
            plain_text += _char
        else:
            plain_text += char
    return plain_text

def solve(encoded: str) -> str:
    for n in range(26):
        decoded = decipher(encoded, n)
        print(decoded)
        sleep(0.2)


if __name__ == '__main__':
    encoded = "c'g ufmi domn u aclf, mnuhxcha ch zlihn iz u vis, umecha bcg ni fipy byl."
    plain_text = "This is a new year!"
    cipher = encipher(plain_text, 11235813213455)
    print('CIPHER', cipher)
    print()
    cipher = open('./2023.txt').read()
    plain = decipher(cipher, 11235813213455)
    print(plain)
    print()
#     solve(encoded)

