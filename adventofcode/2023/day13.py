import pprint

from itertools import starmap

from read_file import read_data

def to_bits(line):
    return ''.join(['1' if l == '#' else '0' for l in line])

def parser(line):
    return [l for l in line.split('\n')]

def solve(blocks, smudge=0):
    total = 0

    for block in blocks:
        def find_mirror(b, mul):
            count = 0
            for i in range(1, len(b)):
                up, down = "".join(b[:i][::-1]), "".join(b[i:])
                if smudge == sum(starmap(lambda a, b: a != b, zip(up, down))):
                    count = i

            if not count:
                return find_mirror(transpose_matrix(b), 1)
            return count * mul

        count = find_mirror(block, 100)
        total += count
    return total


def transpose_matrix(block):
    return tuple("".join(c[::-1]) for c in zip(*block))


if __name__ == '__main__':
    data = read_data('./data/2023/day13_input.txt', parser=parser, sep='\n\n')
    result = solve(data)
    print('PART ONE ====>', result)
    pt_result = solve(data, 1)
    print('PART TWO ====>', pt_result)
