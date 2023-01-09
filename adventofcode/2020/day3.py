from read_file import read_data

def part_one(view, slope):
    dx, dy = slope
    trees_count = 0

    for x, row in enumerate(view[::dy]):
        l = len(row)
        index = (dx * x) % l

        if row[index] == '#':
            trees_count += 1
    return trees_count

def part_two(view):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1

    for slope in slopes:
        trees = part_one(view, slope)
        result *= trees
    return result
        
if __name__ == '__main__':
    filename = '../data/day3_input.txt'
    r = read_data(filename)
    result = part_one(r, (3, 1)), part_two(r)
    print(result)
