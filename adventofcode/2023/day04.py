import re

from read_file import read_data
import pprint

def splitter(str_nums):
    return set(int(i) for i in re.findall(r"\d+", str_nums))

def solve(cards, is_part_two=False):
    total = 0
    copies = {}

    for i, card in enumerate(cards):
        winning, yours = card.split('|')
        _, winning_numbers = winning.split(':')
        f = splitter(winning_numbers) & splitter(yours)
        card_name = f'Card {i + 1}'

        m = len(f)
        if is_part_two:
            # part two
            y = 1
            if card_name in copies:
                # means a copy also wins
                copies[card_name] += y
                y = copies[card_name]
            else:
                copies[card_name] = y

            x = i + 2
            for k in range(m):
                copy_card = f'Card {x}'
                if copy_card in copies:
                    copies[copy_card] += y
                else:
                    copies[copy_card] = y
                x += 1
        else:
            if not f: continue

        n = m - 1
        total += 2**n

    if is_part_two:
        return sum(copies.values())
    return total


if __name__ == '__main__':
    data = read_data("../data/2023/day04_input.txt")
    result = solve(data)
    print("PART ONE: ", result)
    pt_result = solve(data, True)
    print("PART TWO: ", pt_result)
