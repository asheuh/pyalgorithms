def population_count(x: int):
    # This is a naive implementation, shown for comparison,
    # and to help in understanding the better functions.
    # This algorithm uses 24 arithmetic operations (shift, add, and).
    m1  = 0x5555555555555555
    m2  = 0x3333333333333333
    m4  = 0x0f0f0f0f0f0f0f0f
    m8  = 0x00ff00ff00ff00ff
    m16 = 0x0000ffff0000ffff
    m32 = 0x00000000ffffffff
    h01 = 0x0101010101010101

    x = (x & m1 ) + ((x >>  1) & m1 )
    x = (x & m2 ) + ((x >>  2) & m2 )
    x = (x & m4 ) + ((x >>  4) & m4 )
    x = (x & m8 ) + ((x >>  8) & m8 )
    x = (x & m16) + ((x >> 16) & m16)
    x = (x & m32) + ((x >> 32) & m32)
    return x


def population_count_optimized(x: int):
    # count set bits in an integer
    # This is better when most bits in x are 0
    # This algorithm works the same for all data sizes.
    # This algorithm uses 3 arithmetic operations and 1 comparison/branch per "1" bit in x.
    count = 0
    while x:
        x &= (x - 1)
        count += 1
    return count

if __name__ == '__main__':
    count = population_count_optimized(27834499499494)
    print(count)
