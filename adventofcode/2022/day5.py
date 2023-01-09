import re
import pprint

from read_file import read_data
from collections import defaultdict


def rearrange_crates(crates):
    crates = parse_stacks(crates)
    stacks = defaultdict(list)
    n = int(crates[-1][-1])

    for i in range(n):
        for j in range(n - 1, -1, -1):
            char = crates[i][j]
            if char != ' ':
                stacks[i + 1].append(crates[i][j])
    return stacks

def part_one(moves, crates, is_part2=False):
    moves = parse_moves(moves)
    stacks = rearrange_crates(crates)
    for move in moves:
        n, fro, to = move
        if is_part2:
            to_move = stacks[fro][-n:]
            stacks[to].extend(to_move)
            # remove from stacks[from]
            stacks[fro] = stacks[fro][:-n]
        else:
            for _ in range(n):
                stacks[to].append(stacks[fro].pop())
    return ''.join([stacks[key][-1] for key in stacks])

def parse_moves(moves):
    return [tuple(int(i) for i in re.findall(r'\d+', move)) for move in moves] 

def parse_stacks(crates):
    return list(zip(*tuple(item[1::4] for item in crates)))

def parser(line):
    return line.split('\n')


if __name__ == '__main__':
    crates, moves = read_data('../data/2022/crates_input.txt', parser=parser, sep='\n\n')
    res = part_one(moves, crates, True)
    print(res)
