def hamming_distance(x, y):
    if not x or not y:
        return

    if isinstance(x, str) and isinstance(y, str):
        x, y = parse_string(x, y)

    xy_xor = x ^ y
    
    count = 0
    while xy_xor:
        xy_xor &= (xy_xor - 1)
        count += 1
    return count

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
