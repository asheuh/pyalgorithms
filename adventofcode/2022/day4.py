from read_file import read_data


def camp_cleanup(data, is_part2=False):
    n = len(data)
    count = 0

    for item in data:
        f1, f2 = item
        i, j = f1
        x, y = f2

        if not is_part2 and ((x >= i and y <= j) or (i >= x and j <= y)):
            count += 1

        if is_part2 and ((x > j) or (i > y)):
            count += 1

    if is_part2:
        return n - count
    return count

def parse_to_int(line):
    return tuple(int(i) for i in line)

def parser(line):
    return [parse_to_int(item.split('-')) for item in line.split(',')]


if __name__ == '__main__':
    data = read_data('../data/2022/camp_input.txt', parser=parser)
    res = camp_cleanup(data, True)
    print(res)
