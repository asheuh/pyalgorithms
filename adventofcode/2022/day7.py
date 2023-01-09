import re
import pprint

from read_file import read_data

from time import sleep


def find_total(items):
    limit = 100000
    total = 0
    dirs = ['/']

    i = 0
    n = len(items)
    while i < n:
        to_add = 0
        item = items[i]

        if item.startswith('$') and item.split(' ')[1] == 'ls':
            j = i + 1

            while j < n and not items[j].startswith('$') and not items[j].startswith('dir'):
                number = re.findall(r'\d+', items[j])

                if number:
                    num = int(number[0])
                    to_add += num

                    if to_add > limit:
                        to_add = 0
                        break
                i = j
                j += 1
        
        if item.startswith('$') and 'cd' in item:
            _, cd, d = item.split(' ')
            if d == '/':
                dirs = ['/']
            elif d == '..':
                dirs.pop()
            else:
                dirs.append(dirs[-1] + d + '/')
        i += 1
        sleep(.005)
        for dirrr in dirs:
            total += to_add
    return total


if __name__ == '__main__':
    data = read_data('../data/2022/output_input.txt')
    res = find_total(data)
    print(res)
