from utils import ntz

'''
 Finding the next higher number after a given number that has
 the same number of set bits(1-bits)
'''

def snoop(x):
    # Line ones variable can be written the following number of ways
    # - y = r | ((x ^ r) >> (2 + ntz(x))) ntz(x): number of trailing zeros in x
    # - y = r | ((x ^ r) >> (33 - nlz(s))) nlz(s) number of leadinf zeros
    # - y = r | ((1 << (pop(x ^ r) - 2)) - 1) pop(x): population count
    smallest = x & -x
    ripple = smallest + x
    ones = x ^ ripple
    ones = (ones >> (2 + ntz(smallest)))
    return ripple | ones


if __name__ == '__main__':
    x = input('Enter an integer: ')
    nextt = snoop(int(x))
    print(x, "--------->", nextt)
