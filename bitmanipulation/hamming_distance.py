from pyalgorithms.hackersdelight.py.utils import pop 


def hamming_distance(x, y):
    if not x or not y:
        return

    if isinstance(x, str) and isinstance(y, str):
        x, y = parse_string(x, y)

    xy_xor = x ^ y
    return pop(xy_xor)
    
def parse_string(x, y):
    def to_bin(value):
        return ''.join(format(ord(i), 'b') for i in value)

    x_bin = to_bin(x)
    y_bin = to_bin(y)
    return int(x_bin, 2), int(y_bin, 2)

if __name__ == '__main__':
    x = 4
    y = 1
    result = hamming_distance(x, y)
    print(result)
