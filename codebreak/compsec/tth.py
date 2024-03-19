# Toy tetragraph hash
import pprint

from collections import defaultdict

from helpers import *

def tth(text, block_size):
    """Given a message(text) consisting of a sequence of letters,
    tth produces a hash valu consisting of four letters
    """
    text = to_ignore(text).lower()
    num_map = numeric_map()
    n = len(text)
    r = n % block_size
    if r:
        n += r
        text += '*' * r

    blocks = []
    while text:
        block = text[:block_size]
        text = text[block_size:]
        blocks.append(block)

    running_total = [0, 0, 0, 0]
    
    for block in blocks:
        running_total = compression_function(running_total, block)
    return ''.join([num_map[i] for i in running_total])


def rotation(grid):
    ng = list(zip(*list(zip(*reversed(grid)))[::-1])) 
    ng[-1] = list(reversed(ng[-1]))
    return ng

def compression_function(rn, block):
    n = len(block)
    a_map = alpha_map()

    def compute_rn(rn, g, rotate=False):
        i = 0
        k = 4
        grid = g
        grid_sum = defaultdict(int)

        while not rotate and k <= n:
            row = [a_map[block[i]] for i in range(i, k)]
            grid.append(row) 
            i = k
            k += 4

        if rotate:
            grid = rotation(grid)

        transposed = zip(*grid)
        for i, row in enumerate(transposed):
            rn[i] = ((sum(row) % 26) + rn[i]) % 26
        return rn, grid

    rn, grid = compute_rn(rn, [])
    rn, grid = compute_rn(rn, grid, True)
    return rn


if __name__ == '__main__':
    text = 'I leave twenty million dollars to my friendly cousin Bill.'
    result = tth(text, 16)
    print(result)
