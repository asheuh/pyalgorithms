import re
import pprint
import copy

from time import sleep
from read_file import read_data

def process_data(boards):
    numbers = [num for num in next(iter(boards))[0]]
    return numbers, {bi + 1: board for bi, board in enumerate(boards[1:])}

def find(_list, key):
    for i, v in enumerate(_list):
        if v == key:
            return i, True
    return None, False
        

def part_one(boards, intentional_loss=False):
    def sum_ints(value):
        return sum(int(x) for x in value if x != 'MARKED')

    numbers, boards = process_data(boards)
    dcboards = copy.deepcopy(boards)
    n = len(boards)
    stack = [*list(boards.keys())]
    won = False
    last_number = result = None

    while not won:
        board_number = stack.pop()
        number = numbers[0]
        a, b, c, d, e = board_rows = boards[board_number]
        board_cols = [list(item) for item in zip(a, b, c, d, e)]
        test_row = test_col = True

        if not stack and numbers:
            # reset stack and delete number for numbers if cycle is complete for that number
            stack = [*list(boards.keys())]
            numbers = numbers[1:]

        for index in range(5):
            row = board_rows[index]
            col = board_cols[index]
            
            # number in row and col and return it's index with found status
            rm_i, rfound = find(row, number)
            cm_i, cfound = find(col, number)

            if rfound:
                row[rm_i] = 'MARKED' # mark number as called in row
                board_cols[rm_i][index] = 'MARKED' # also mark the corresponding col
                test_row = row
                test_col = board_cols[rm_i]
                break
            elif cfound:
                col[cm_i] = 'MARKED'
                board_rows[cm_i][index] = 'MARKED'
                test_col = col 
                test_row = board_rows[cm_i]
                break

        if not isinstance(test_row, bool) and not ({'MARKED'} ^ set(test_row)) or \
                not isinstance(test_col, bool) and not ({'MARKED'} ^ set(test_col)):
            last_number = number
            result = boards[board_number]
            won = True

            if intentional_loss:
                won = False # We want to continue process until we find a board that wins last
                del boards[board_number] # delete the winning board
                stack = [*list(boards.keys())]
                if not stack: # We have found the last board to win; stored in result variable
                    won = True

    return sum([sum_ints(i) for i in result if i]) * int(last_number)

def part_two(boards):
    return part_one(boards, True)

def to_dict(tupl):
    return {v: i for i, v in enumerate(tupl)}

def parser(section): 
    return [re.findall(r'(\d+)', item) for item in section.split('\n')]


if __name__ == '__main__':
    data = read_data('data/2021/day4_input.txt', parser=parser, sep='\n\n')
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1, result_p2)
