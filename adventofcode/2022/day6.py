from read_file import read_data
from time import sleep


def subroutine(datastream, is_part2=False):
    n = len(datastream)
    result = 0
    rang = 4

    if is_part2:
        rang = 14

    for i in range(n):
        chars = set(datastream[i: i + rang])
        if len(chars) == rang:
            result = len(datastream[:i + rang])
            break
    return result

if __name__ == '__main__':
    data = read_data('../data/2022/datastream_input.txt')
    res = subroutine(data[0], True)
    print(res)
