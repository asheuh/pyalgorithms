import re
import string
from typing import List, Dict

from encoding import split_in_twos



class XORDecryptor:
    def __init__(self, cipher: str, key_length: int, words: Dict[str,bool]):
        self.cipher = cipher
        self.key_length = key_length
        self.words = words

    def xor_crypto(self):
        _xor_codes = [int(i, 16) for i in split_in_twos(self.cipher, 2)] 
        xor_codes = self.groups_of_keylen(_xor_codes, self.key_length)
        codes = string.ascii_lowercase + string.ascii_uppercase + '0123456789'

        all_possible_keys = []
        for x in xor_codes:
            results = []
            for c in codes:
                k = ord(c)
                if self.check_ascii_to_char(x, k):
                    results.append(c)

            if results:
                all_possible_keys.append(results)
            else:
                all_possible_keys.append(['G']) # Manual guess

        key_count = 1
        for key in all_possible_keys:
            key_count *= len(key)
        return self.decode(_xor_codes, all_possible_keys, key_count)

    @staticmethod
    def check_ascii_to_char(asciis, k):
        for code in asciis:
            ch = chr(code ^ k)
            if not re.match(r"[\w ,.'!]", ch):
                return False
        return True

    @staticmethod
    def groups_of_keylen(xor_codes, keylen):
        grid = [[] for _ in range(keylen)]
        i = 0
        for b in xor_codes:
            grid[i].append(b)
            i += 1
            if i >= keylen:
                i = 0
        return grid
            

    def decode(self, xors, keys, count):
        encryption_key = ''
        decrypted = ''

        for i in range(count):
            key = self.generate_key(keys, i)
            sentence = self.xor_decrypt(xors, key)
            print(sentence)
            print()
            print(key)

            has_common_words = True
            for word in sentence.split(' '):
                if not self.words.get(word):
                    has_common_words = False

            if has_common_words:
                encryption_key = key
                decrypted = sentence
                break
        return (encryption_key, decrypted)

    @staticmethod
    def xor_decrypt(xors, key):
        result = ''
        i = 0
        for xor in xors:
            ch = chr(xor ^ ord(key[i]))
            result += ch
            i += 1
            if i >= len(key):
                i = 0
        return result

    @staticmethod
    def generate_key(keys, i):
        result = ''
        for key in keys:
            n = len(key)
            index = int(i % n) 
            result += key[index]
            i -= index
            i /= n
        return result


if __name__ == '__main__':
    cipher = '1e3b65333607713a2624201b383a2b346121713d24312448333020296109223e20236d48761c23673807247535323548383b3128611c3930652a200b393c2b22611f233a2b20610e38323035241b7d75322e2d0471212d22611a38322d3361093f263222331b71362a2a24483e2031786648711c65262c483f3a3167200a3d306535280f3921293e611c3e752437311a343d20292548253d20672a013f3165282748323a2b21341b383a2b672e0e713c2122201b71212d263548323a302b254821272a312e0334753632220071346536340d22212c282f46'
    words = open('data/words.txt').read().split('\n')
    WORDS = {k.lower(): True for k in words}
    xor_decryptor = XORDecryptor(cipher, 6, WORDS)
    key, sentence = xor_decryptor.xor_crypto()
    print('-' * (len(sentence) + 11))
    print("Decrypted:", sentence)
    print('Key:', key)
    print('-' * (len(sentence) + 11))
