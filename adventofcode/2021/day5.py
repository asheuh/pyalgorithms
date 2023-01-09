import re
import pprint
from time import sleep

from read_file import read_data


def part_one(lines, consider_diagonal=False):
    def draw_points(i, d, reverse, diagonal, sign, alt, v, f, g, naon):
        x, y = i, d
        if reverse:
            x, y = d, i
        if diagonal:
            x, y = i, i + (sign * d)
        if alt:
            x, y = i, abs((i - v) - f)
        if naon:
            print('UFHIHFHUIASDFHAJSHDSA')
            x, y = i, g - i
        return x, y
    
    points = []

    for line in lines:
        curr, target = line
        x1, y1 = curr
        x2, y2 = target
        j, k = (x2 - x1), (y2 - y1)
        diagonal = alt = naon = False
        f = v = g = int()

        # Ignore diagonal
        if (x1 != x2) and (y1 != y2):
            if not consider_diagonal:
                continue

#             if ((x1 > x2) and (y1 > y2)) or ((x1 < x2) and (y1 < y2)):
            start, end, e, d = x1, x2, j, abs(x1 - y1)
            diagonal = True

            if (y1 - x1) > 0 < (y2 - x2) and (start > end):
                d = -d

            elif (y1 == x1 and x2 != y2) or (y1 != x1 and x2 == y2):
                alt = True
                t = abs(j) + abs(k)
                h = abs(j)

                if (x1 - y1) < 0 or (x2 - y2) < 0:
                    f = (t + 1 + t)
                    v = -h
                else:
                    f = (t + 1) 
                    v = h

            elif ((x1 > x2) and (y1 < y2)) or ((x1 < x2) and (y1 > y2)):
                naon = True
                if end > start:
                    g = end
                else:
                    g = start
                print('HEHEHHE')

            print(start, end, d, e)
        
#         try:
#             prev_count = count
#             c, _, stack = seen[curr]
#             stack.sort()
#             des = stack[-1]
#             a, b = des
# 
#             if a == x2:
#                 v, m, coms = max(b, y2), min(b, y2), y1
#             else:
#                 v, m, coms = max(a, x2), min(a, x2), x1
# 
#             c += 1
#             count = ((v - coms) + 1) - abs(v - m)
# 
#             if c > 2:
#                 count = prev_count + (count - prev_count) 
# 
#                 if count < prev_count:
#                     count = prev_count
# 
#             stack.append(target)
#             seen[curr] = (c, target, stack)
#         except Exception as e:
#             seen[curr] = (1, target, [target])

        reverse = False

        if y2 == y1:
            d, e = y1, j
            start, end = x1, x2
        elif x2 == x1:
            d, e = x1, k
            start, end = y1, y2
            reverse = True

        sign = -1 if e < 0 else 1 

        point = [
            draw_points(i, d, reverse, diagonal, sign, alt, v, f, g, naon)
            for i in range(start, end + sign, sign)
        ]
        print(f'{line} ===> {point}')
        print(sign)
        points += point
    return counter(points)

def counter(points):
    count = 0
    seen = {}
    for point in points:
        try:
            c, counted = seen[point]
            c += 1

            if c > 1 and not counted:
                count += 1
                seen[point] = (c, True)
        except Exception as e:
            seen[point] = (1, False)
    return count

def parser(section):
    return [
        tuple(int(point) for point in coords.split(','))
        for coords 
        in re.findall(r'[0-9]+,[0-9]+', section)
    ]

def part_two(lines):
    return part_one(lines, True)

if __name__ == '__main__':
    data = read_data('data/2021/day5_input.txt', parser=parser) 
    result_p1 = part_two(data)
    print(result_p1)
