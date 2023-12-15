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
        ir = len(rd[-1]) - 1
        ci = 0
        irs = []
        while ir >= 0:
            if rd[-1][ir] == '#':
                ci += 1
                irs.append(ir)

            ir -= 1

        print('SLJKDSDKSKDKALDLSDK92138123809218308213', ci, irs, rd)
        if irs and ci <= group[-1]:
            a = len(rd[-1])
            bb = a - irs[0] - 1 # first
            cc = a - irs[-1] + 1 # last
            print(bb, cc, a)
            if bb > group[-1]:
                rd[-1] = rd[-1][:-bb]
                group.pop()

            if (irs[0] - irs[-1] - 1) > 0:
                rd[-1] = rd[-1][:-(bb+2)]
                group.pop()
            else:
                print('SKJSJD0', rd)
                rd[-1] = rd[-1][:irs[-1]]
                print('SOOOOOO', rd)
                group.pop()

            if len(irs) == 1:
                _rr = irs[0]
                rd[-1] = rd[-1][:-ir]

        if not group: continue

        lr = len(rd)
        while rd and len(rd[lr-1]) < group[-1]:
            rd.pop()
            lr -= 1

        while group and rd and group[0] == len(rd[0]):
            group.pop(0)
            rd.pop(0)
            if not group or not rd:
                total+=1
                break

        if not rd: continue
        print('SDJJASD', rd)
        k = [len(x) for x in rd]
        f = ['0' if a == '?' else '1' for a in ''.join(rd)]
        print(f)
        r = []
        if not all([c == '0' for c in f]) and is_palindrome(f):
            total += 1
            continue

        g = []
        up, upx = (False, 0)
        down, downx = (False, 0)
        if len(rd) == 1:
            total += 1
            continue

        while group:
            q = group.pop(0)
            j = x = i = v = 0

            while i < q:
                while x < q and i < len(f) and f[i] == '1':
                    j += 1
                    i += 1

                print('HHHHHIHOHOH',j,x)
                if (j + x) == q and x >= j:
                    up, upx = (True, x)

                if x < j and (x + j != q):
                    down, downx = (True, j)
                    print('------????',x, j, q, f)

                if i >= q:
                    break

                print(i, f)
                f[i] = '1'
                print('FFFFF', f)
                x += 1
                i += 1

            if q  == j or (j + x) == q and x >= j:
                print('dskfjfjdk', j, q, group, r, f)
                v = 1

            print('oooooooo>',j, x, r)
            r.extend(f[:j + v + x])
            f = f[j + v + x:]
            print('JJJJJ-->', r, j, q, x, f)

            g.append(q)
            if j == q:
                g.pop()
                r = []
            print('=++++++++++> ', r, j, q, x, f)

        if not r and not f:
            continue

        r = r + f
        print('rrrr ------->', r, f, upx)
        if is_palindrome(r):
            total += 1
            continue
        
        _r = ''.join(r)
        r = ''.join(reversed(_r))
        if int(r, 2) > int(_r, 2):
            r = _r

        print('total', total, r, g)
        l = len(r)
        prev = int(r, 2)
        m = [len(u) for u in r.split('0') if u]
        added = False
        if m == g:
            print('0sdjhlsajdljsad')
            added = True
            total += 1

        print('RRDGUPXDOWNX',r, rd, g, upx, downx, r, down)
        if (downx > 0 and down):
            print('----->print', downx)
            if added:
                total -= 1
            r = r[downx:]
            print(total)

        print('up', up, upx, l, len(str(int(r))))
        if up and not (l - len(str(int(r))) <= upx):
            print('SKJDSDJ')
            total -= 1

        while 1:
            p = find_next(prev)
            if len(bin(p)[2:]) > l:
                break

            h = bin(p)[2:]
            m = [len(u) for u in h.split('0') if u]
            if m == g:
                print('------>', h)
                total += 1
#                 if ''.join(reversed(h)) == r:
#                     print('POPOPOPPOPOP', h)
#                     break

#                 if len(h) == l and h.endswith('1'):
#                     total -= 1
                if up and not (l - len(h) <= upx):
                    total -= 1

            else:
                kn = len(k) - 1
                kk = k[kn]
                is_pal = False
                while (
                    len(h) > kk and len(rd) > 1
                ) and (h[-kk-1] == h[-kk] == h[-kk] == '1'):
                    print('JSJHJSJS', h)
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


import sys
import functools

# Read the puzzle input
# Trim whitespace on either end
output = 0

@functools.lru_cache(maxsize=None)
def calc(record, groups):

    # Did we run out of groups? We might still be valid
    if not groups:

        # Make sure there aren't any more damaged springs, if so, we're valid
        if "#" not in record:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that we can't fit
            return 0

    # There are more groups, but no more record
    if not record:
        # We can't fit, exit
        return 0

    # Look at the next element in each record and group
    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as pound
    def pound():

        # If the first is a pound, then the first n characters must be
        # able to be treated as a pound, where n is the first group number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        # If the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if record[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return calc(record[next_group+1:], groups[1:])

        # Can't be handled, there are no possibilites
        return 0

    # Logic that treats the first character as a dot
    def dot():
        # We just skip over the dot looking for the next pound
        return calc(record[1:], groups)

    if next_character == '#':
        # Test pound logic
        out = pound()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + pound()

    else:
        raise RuntimeError

    print(record, groups, out)
    return out


# Iterate over each row in the file
data = read_data('./data/2023/day12_input.txt', parser=parser)
for record, raw_groups in data:

    # Split into the record of .#? record and the 1,2,3 group
#     record, raw_groups = entry.split()

    # Convert the group from string 1,2,3 into a list
    groups = [int(i) for i in raw_groups.split(',')]

    output += calc(record, tuple(groups))

    # Create a nice divider for debugging
    print(10*"-")


print(">>>", output, "<<<")
result = solve(data)
print('PART ONE ===> ', result)


# if __name__ == '__main__':
#     data = read_data('./data/2023/day12_input.txt', parser=parser)
#     result = solve(data)
#     st = time()
#     et = time()
#     print('PART ONE ===> ', result)
#     print('TIME TAKEN ====>', et-st)
