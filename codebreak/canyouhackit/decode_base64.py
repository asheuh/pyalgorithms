import base64
from encoding import split_in_twos

def read_file(filename):
    return open(filename)

def create_file(encoded_file: str):
    with open('data/output.zip', 'wb') as f:
        base64.decode(encoded_file, f)

def decode():
    flag = split_in_twos(read_file('data/flag.txt').read(), 2) 
    xor_key = split_in_twos(read_file('data/xor_key.txt').read()) 
    text = ''

    for x, y in zip(flag, xor_key):
        k = int(x, 16)
        char = chr(k ^ ord(y))
        text += char
    return text
    
if __name__ == '__main__':
    encoded = read_file('base64.txt')
    create_file(encoded)
    d = decode()
    print(d)
