import math
from read_file import read_data

def calculate_seat_id(seat_number):
    rows = 128 - 1
    columns = 8 - 1
    rules = {
            'F': lambda v: (v[0], math.floor((v[0] + v[1]) / 2)),
            'B': lambda v: (math.ceil((v[0] + v[1]) / 2), v[1]),
            'R': lambda v: (math.ceil((v[0] + v[1]) / 2), v[1]),
            'L': lambda v: (v[0], math.floor((v[0] + v[1]) / 2))}
    a, b = 0, rows
    x, y = 0, columns
    row = 0
    column = 0

    for letter in seat_number:
        if letter in {'R', 'L'}: 
            x, y = rules[letter]((x, y))
            if x == y:
                column = x
        else:
            a, b = rules[letter]((a, b))
            if a == b:
                row = a
    seat_id = (row * 8) + column
    return seat_id

def part_one(seat_numbers):
    return max(seat_numbers)

def part_two(seat_numbers):
    seat_ids = seat_numbers 
    sorted_ids = sorted(seat_ids)
    l = len(sorted_ids)
    my_seat = 0

    for i in range(l):
        j = i + 1
        if j < l:
            m = sorted_ids[j]
            n = sorted_ids[i]
            k = m - n 

            if k > 1:
                a = m - 1
                b = n + 1

                if a == b:
                    my_seat = a
    return my_seat


if __name__ == '__main__':
    filename = '../data/day5_input.txt'
    seat_numbers = read_data(filename, calculate_seat_id)
    result = part_one(seat_numbers), part_two(seat_numbers)
    print(result)

