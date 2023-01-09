import pprint
import math
from time import sleep


ALPHASIZE = 4
BITMAX = 128
BITMASk = [0x55555555, 0x33333333, 0x0f0f0f0f, 0x00ff00ff, 0x0000ffff]
WLEN = 32 # Word length
NWORDS = 0
A_STRINGS = [[0] * BITMAX for _ in range(ALPHASIZE)]

def lcs(x, y, scs=False):
    # longest common subsequence
    m = len(x)
    n = len(y)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # create a matrix table

    for r in range(0 if scs else 1, m + 1):
        for c in range(0 if scs else 1, n + 1):
            if scs:
                if not r:
                    table[r][c] = c
                    continue
                elif not c:
                    table[r][c] = r
                    continue

            if x[r - 1] == y[c - 1]: # Python zero indexing
                table[r][c] = table[r - 1][c - 1] + 1
            else:
                if scs:
                    table[r][c] = 1 + min(table[r][c - 1], table[r - 1][c])
                else:
                    table[r][c] = max(table[r][c - 1], table[r - 1][c])

    k = table[m][n]
    if scs:
        return backtrack_iterative(table, x, y, (m, n), k, True), k 
    return backtrack_iterative(table, x, y, (m, n), k), k 

def backtrack_iterative(table, x, y, mn, k, scs=False):
    lcs_string = ''
    i, j = mn
    if scs:
        index = k
        scs_string = [''] * index

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            table[i][j] = 0
            i -= 1
            j -= 1
            lcs_string = x[i] + lcs_string
            if scs:
                index -= 1
                scs_string[index] = x[i]
            continue
            # return backtrack(table, x, y, i - 1, j - 1) + x[i - 1]

        if table[i][j - 1] > table[i - 1][j]:
            if scs:
                i -= 1
                index -= 1
                scs_string[index] = x[i]
            else:
                j -= 1
        else:
            if scs:
                j -= 1
                index -= 1
                scs_string[index] = y[j]
            else:
                i -= 1
            # return backtrack(table, x, y, i, j - 1)
    if scs:
        while i > 0:
            i -= 1
            index -= 1
            scs_string[index] = x[i]

        while j > 0:
            j -= 1
            index -= 1
            scs_string[index] = y[j]
        return ''.join(scs_string)
    return lcs_string

def backtrack_recursion(table, x, y, i, j):
    if i == 0 or j == 0:
        return ""

    if x[i - 1] == y[j - 1]:
        return backtrack_recursion(table, x, y, i - 1, j - 1) + x[i - 1]
    
    if table[i][j - 1] > table[i - 1][j]:
        return backtrack_recursion(table, x, y, i, j - 1)
    return backtrack_recursion(table, x, y, i - 1, j)


def lcs_fast(x, y):
    # This is based on The Hunt-Szymanski Algorithm for LCS
    # Papers:
    #   - https://imada.sdu.dk/~rolf/Edu/DM823/E16/HuntSzymanski.pdf
    #   - https://cse.hkust.edu.hk/mjg_lib/bibs/DPSu/DPSu.Files/HuSz77.pdf
    # Applications:
    #   - Finding the longest ascending subsequence of a permutation
    #     of the integers from 1 to n
    #   - Finding a maximum cardinality linearly ordered subset of some
    #     finite collection of vectors in 2-space
    #   - Finding the edit distance between two files in which the individual
    #     lines of the files are considered to be atomic. The longest common
    #     subsequence of these files, considered as sequences, represents that
    #     common "core" which does not have to be changed if we desire to edit 
    #     one file into the other 
    m = len(x)
    n = len(y) 
    NWORDS = (m + WLEN - 1) // WLEN;
    alphastrings(x, m)
    bit1 = [0] * NWORDS
    pstring = y

    for i in range(1, n + 1):
        pass
    print(bit1)
    return

def alphastrings(s, l):
    for i in range(ALPHASIZE):
        for j in range(NWORDS):
            A_STRINGS[i][j] = 0

    p = s
    j = l
    for i in range(ALPHASIZE):
        for j in range(l - 1, -1, -1):
            if j & 1:
                print("%1x", (A_STRINGS[i][j // WLEN] >> (j % WLEN)) & 1)
            else:
                print("%1x ", (A_STRINGS[i][j // WLEN] >> (j % WLEN)) & 1)
        print()


if __name__ == '__main__':
    x = 'ABCDEFG'
    y = 'BCDGK'
    result = lcs_fast(x, y)
    print(result)

