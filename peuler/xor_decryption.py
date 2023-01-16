from itertools import permutations
from string import ascii_lowercase, ascii_uppercase


def xor_decryption(codes):
    alphabets = ascii_lowercase
    alphabets2 = ascii_uppercase
    perms = permutations(alphabets, 3)
    results = []
    plain_text = ''
    common_words = ['and', 'the', 'is']

    for perm in perms:
        encrypt_key = [ord(i) for i in perm]
        decrypt_codes = []

        for index, code in enumerate(codes):
            decrypt =  encrypt_key[index % 3] ^ code
            decrypt_codes.append(decrypt)

        decrypted_text = ''.join(chr(i) for i in decrypt_codes)
        
        has_common_words = True
        for word in common_words:
            a = decrypted_text
            if f' {word} ' not in a:
                has_common_words = False

        if has_common_words:
            plain_text = decrypted_text
            results = decrypt_codes
            break
    return plain_text, sum(results)


if __name__ == '__main__':
    codes = [int(i) for i in open('p059_cipher.txt').read().rstrip().split(',')] 
    res = xor_decryption(codes)
    print(res)
