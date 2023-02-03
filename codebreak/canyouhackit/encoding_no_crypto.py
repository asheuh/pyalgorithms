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

    n = len(decoded)
    prev = 0
    hexpair = []
    # Spiliting in pairs of 2
    for i in range(2, n + 1, 2):
        pair = decoded[prev: i]
        prev = i
        hexpair.append(pair)
    return hexpair

def decode(seq: list):
    return ''.join(chr(int(c, 16)) for c in seq)


encoded = "QlpoOTFBWSZTWS+qfEEAAHNYAEAAQABgACAAcDNNBJ6pHeAzEBcuoZksRGTSbFlBUqMWyaxmVSVoGjWe1bmzT4u5IpwoSBfVPiCA"
decoded = encoding(encoded)
d = decode(decoded)
print(d)
