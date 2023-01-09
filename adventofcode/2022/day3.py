import string

from read_file import read_data

lower_map = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
}
upper_map = {
        'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31,
        'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
        'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41,
        'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
        'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51,
        'Z': 52
}


def part_two(group):
    lower_ascii = string.ascii_lowercase
    upper_ascii = string.ascii_uppercase
    total = 0

    for i in range(26):
        # check lowercase
        char = lower_ascii[i]
        res = []

        for item in group:
            if {char} & item:
                res.append(char)

        if len(res) == 3:
            total += lower_map[char]
        else:
            # check uppercase
            char = upper_ascii[i]
            res = []

            for item in group:
                if {char} & item:
                    res.append(char)

            if len(res) == 3:
                total += upper_map[char]
    return total

def rucksack(items, is_part2=False): 
    total = 0
    group = []

    for i, item in enumerate(items):
        index = i + 1
        c1, c2 = item
        c1_set = set(c1)
        c2_set = set(c2)
        common = c1_set & c2_set
        group.append(set(c1 + c2))

        if is_part2 and not index % 3:
            total += part_two(group)
            group = [] # reset group

        if not is_part2 and common:
            item_type = common.pop()

            if item_type in upper_map:
                total += upper_map[item_type]

            if item_type in lower_map:
                total += lower_map[item_type]
    return total

def parser(line):
    n = len(line)
    mid = n >> 1
    return (line[:mid], line[mid:])


if __name__ == '__main__':
    items = read_data('../data/2022/bp_input.txt', parser=parser)
    res = rucksack(items, True)
    print(res)
