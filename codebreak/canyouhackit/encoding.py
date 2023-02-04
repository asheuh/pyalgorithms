import codecs
import bz2

def encoding(encoded: str) -> list:
    encoded = codecs.decode(encoded.encode('utf-8'), encoding='base64')
    decompressed = bz2.decompress(encoded) # Returns byte of binary numbers
    bins = decompressed.decode().split(' ')
    decoded = ''

    # converting binary to base 2 integer and to character
    for binary in bins:
        k = int(binary, 2)
        decoded += chr(k)
    return split_in_twos(decoded, 2)

def split_in_twos(decoded: str, k=1):
    # Spiliting in pairs of 2
    n = len(decoded)
    prev = 0
    for i in range(k, n + 1, k):
        pair = decoded[prev: i]
        prev = i
        yield pair

def _decode(seq: list):
    return ''.join(chr(int(c, 16)) for c in seq)


if __name__ == '__main__':
    encoded = "QlpoOTFBWSZTWS+qfEEAAHNYAEAAQABgACAAcDNNBJ6pHeAzEBcuoZksRGTSbFlBUqMWyaxmVSVoGjWe1bmzT4u5IpwoSBfVPiCA"
    decoded = encoding(encoded)
    d = _decode(decoded)
    print(d)

