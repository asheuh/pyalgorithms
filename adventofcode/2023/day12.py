import re
import pprint

from time import sleep, time

from read_file import read_data


def parser(line):
    return tuple(line.split(' ')) 

def fnumbers(g):
    return [int(i) for i in re.findall(r'\d+', g)] 

def solve(data):
    records = [(r, fnumbers(g)) for r, g in data]
    total = 0

    for record, group in records:
        # find all possible arrangements
        rd = [a for a in record.split('.') if a]

        while group[-1] == len(rd[-1]):
            group.pop()
            rd.pop()
            if not group or not rd:
                total += 1
                break

        if not rd: continue
        if not group: continue

        while group[0] == len(rd[0]):
            group.pop(0)
            rd.pop(0)
            if not group or not rd:
                total+=1
                break

        k = [len(x) for x in rd]
        f = ['0' if a == '?' else '1' for a in ''.join(rd)]
        r = []
        if not all([c == '0' for c in f]) and is_palindrome(f):
            total += 1
            continue

        g = []
        while group:
            q = group.pop(0)
            j = x = i = v = 0

            while i < q:
                while x < q and i < len(f) and f[i] == '1':
                    j += 1
                    i += 1

                if i >= q:
                    break

                f[i] = '1'
                x += 1
                i += 1

            if len(rd) == 1:
                v = 1

            r.extend(f[:j + v + x])
            f = f[j + v + x:]

            g.append(q)
            if j == q:
                g.pop()
                r = []

        r = r + f
        if is_palindrome(r):
            total += 1
            continue
        
        r = ''.join(reversed(r))
        l = len(r)
        prev = int(r, 2)
        m = [len(u) for u in r.split('0') if u]
        if m == g:
            total += 1

        while 1:
            p = find_next(prev)
            if len(bin(p)[2:]) > l:
                break

            h = bin(p)[2:]
            m = [len(u) for u in h.split('0') if u]
            if m == g:
                total += 1

            else:
                kn = len(k) - 1
                kk = k[kn]
                is_pal = False
                while (
                    len(h) > kk and len(rd) > 1
                ) and (h[-kk-1] == h[-kk] == h[-kk] == '1'):
                    h = h[:-kk]
                    kn -= 1
                    kk = k[kn]
                    is_pal = True

                if is_pal:
                    total += 1

            prev = p
    return total

def find_next(x):
    """
    Finding the next higher number after a given number that has
    the same number of set bits(1-bits)
    """
    def ntz(s):
        lookup = [
            32, 0, 1, 26, 2, 23, 27, 0,
            3, 16, 24, 30, 28, 11, 0, 13,
            4, 7, 17, 0, 25, 22, 31, 15,
            29, 10, 12, 6, 0, 21, 14, 9,
            5, 20, 8, 19, 18
        ]
        return lookup[s % 37]

    smallest = x & -x # Isolate learst significant bit
    # turn the clear just before all the rightmost contiguous set bits in x
    # e.g x = 0111 then ripple = 1000
    ripple = x + smallest
    ones = x ^ ripple
    ones >>= (2 + ntz(smallest)) # ntz(x): Number of trailling zeros in x or (ones >> 2) // smallest
    return ripple | ones

def is_palindrome(line):
    n = len(line)

    i = 0
    j = n - 1
    
    while i <= j:
        if line[i] != line[j]:
            return False

        i += 1
        j -= 1
    return True



if __name__ == '__main__':
    data = read_data('./data/2023/day12_input.txt', parser=parser)
    result = solve(data)
    st = time()
    et = time()
    print('PART ONE ===> ', result)
    print('TIME TAKEN ====>', et-st)
