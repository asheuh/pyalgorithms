def pop(x):
    count = 0
    while x != 0:
        count += 1
        x &= (x - 1)
    return count

def pop_one(x):
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x & 0x0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F)
    x = (x & 0x00FF00FF) + ((x >> 8) & 0x00FF00FF)
    x = (x & 0x0000FFFF) + ((x >> 16) & 0x0000FFFF)
    return x

def pop_two(x):
    # Shift right and subtrac (x - SUMMATION[31,i=1] (x >> i))
    total = x
    while x != 0:
        x >>= 1
        total -= x
    return total


def pop_compare(xp, yp):
    x = xp & ~yp # Clear bits where
    y = yp & ~xp # both are 1
    while 1:
        if x == 0:
            z = y | -y
            if z < 0:
                return ('pop Y', z)
            return ('pop X == pop Y', z)
        if y == 0:
            return ('X', 1)
        x = x & (x - 1) # clear one bit
        y = x & (y - 1) # from each


def pop_diff(x, y):
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    y = ~y
    y = y - ((y >> 1) & 0x55555555)
    y = (y & 0x33333333) + ((y >> 2) & 0x33333333)
    x = x + y
    x = (x & 0x0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F)
    x = x + (x >> 8)
    x = x + (x >> 16)
    return (x & 0x0000007F) - 32

if __name__ == '__main__':
    x = 52
    y = 62
    c = pop_diff(x, y)
    print(c)
