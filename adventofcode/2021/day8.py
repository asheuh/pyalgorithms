import re, pprint

from read_file import read_data


def part_one(signals):
    unique_digits = {2: 1, 4: 4, 3: 7, 7: 8} # well, because it's cheaper to loop over a dict in py
    result_count = 0

    for signal in signals:
        usps, output = signal
        for key, value in output.items():
            if not usps[key]:
                continue

            seg_count, _, _ = usps[key]
            out_count, count, _ = value
            if out_count in unique_digits:
                result_count += count
    return result_count

def part_two(signals):
    digits = {2: 1, 4: 4, 3: 7, 7: 8} # well, because it's cheaper to loop over a dict in py
    seen = {i: None for i in range(10)}
    total = 0

    def insert_at_index(indices, value, out):
        for i in indices:
            out[i] = value
        return out

    for signal in signals:
        usps, output = signal
        _out = [''] * 4

        for key, value in usps.items():
            l = len(key)

            if l in digits:
                v = digits[l]
                seen[v] = set(key)

        for key in set([us for us in usps if len(us) == 6]):
            if len(set(key).difference(seen[1])) == 5:
                seen[6] = set(key)
            elif set(key).issuperset(seen[4]):
                seen[9] = set(key)
            else:
                seen[0] = set(key)

        for key in set([us for us in usps if len(us) == 5]):
            if len(set(key).difference(seen[4])) == 3:
                seen[2] = set(key)
            else:
                if set(key).issuperset(seen[1]):
                    seen[3] = set(key)
                else:
                    seen[5] = set(key)

        for item, value in output.items():
            for k, v in seen.items():
                if v == set(item):
                    _, _, indices = value
                    indices = insert_at_index(indices, str(k), _out)
        total += int(''.join(_out))
    return total

def sort(item):
    return ''.join(sorted(item))

def parser(section):
    entries = re.findall(r'\w+', section)
    def to_dict(entry):
        seen = {}
        for i, item in enumerate(entry):
            key = sort(item)
            try:
                item_len, count, indices = seen[key]
                count += 1
                indices.append(i)
                seen[key] = (item_len, count, indices)

            except Exception as e:
                seen[key] = (len(key), 1, [i])
        return seen 
    return to_dict(entries[:-4]), to_dict(entries[-4:])


if __name__ == '__main__':
    data = read_data('data/2021/day8_input.txt', parser=parser)
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1, result_p2)
