import re
import math
import pprint

from time import time


from read_file import read_data


def parser(line):
    return line.split('\n')

def parse_parts(ratings):
    parts = []
    for rating in ratings:
        d = dict(t(kv_str) for kv_str in rating[1:-1].split(','))
        parts.append(d)
    return parts

def parse_workflows(workflows):
    wfs = {}
    for wf in workflows:
        p, s = wf.split('{')
        wfs[p] = s[:-1].split(',')
    return wfs

def t(strr):
    kv = strr.split('=')
    return kv[0], int(kv[1]) 

def matcher(cv, part):
    check, value = cv.split(':')
    cop = check[:2]

    match cop:
        case 'x>':
            return check_part(check, part, '>', value)
        
        case 'x<':
            return check_part(check, part, '<', value)
        case 'm>':
            return check_part(check, part, '>', value)

        case 'm<':
            return check_part(check, part, '<', value)
        
        case 's<':
            return check_part(check, part, '<', value)

        case 's>':
            return check_part(check, part, '>', value)

        case 'a>':
            return check_part(check, part, '>', value)

        case 'a<':
            return check_part(check, part, '<', value)

        case _:
            return False, value

def parse_wf(wf):
    check, t = wf.split(':')
    matched = re.findall(r'(\w)(<|>)(\d+)', check)[0]
    return matched, t

def check_part(check, part, op, value):
    k, v = check.split(op)
    thisv = part.get(k)
    return thisv > int(v) if op == '>' else thisv < int(v), value

def solve_part_one(data):
    workflows, parts = data
    parts = parse_parts(parts)
    workflows = parse_workflows(workflows)
    k = 0
    n = len(parts)
    start = 'in'
    accepted = []
    
    while k < n:
        part = parts[k]
        wfs = workflows[start]
        i = 0
        l = len(wfs)

        while i < l - 1:
            wf = wfs[i]

            matched, value = matcher(wf, part)
            if matched:
                start = value
                break
            else:
                start = wfs[-1]
            i += 1

        if start == 'A':
            accepted.append(part)

        if start not in ['A', 'R']:
            continue

        start = 'in'
        k += 1
    return sum(sum(p.values()) for p in accepted)

def solve_part_two(data):
    workflows, _ = data
    workflows = parse_workflows(workflows)
    ranges = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000),
    }
    def search(start, _ranges, stack):
        wfs = workflows[start]
        fallback = wfs.pop()

        for wf in wfs:
            (c, op, num), target = parse_wf(wf)
            assert int(num)
            num = int(num)
            this_range = _ranges[c]
            low, high = this_range
            hlmatched, _ = smatcher(op, num, (high, low))
            if hlmatched:
                continue
            
            lhmatched, to_thru = smatcher(op, num, (low, high))
            if not lhmatched:
                stack.appned((target, _ranges))
                return stack

            to, thru = to_thru
            _ranges[c] = thru
            c_ranges = _ranges.copy()
            c_ranges[c] = to
            stack.append((target, c_ranges))

        stack.append((fallback, _ranges))
        return stack

    stack = [('in', ranges)]
    total = 0
    while stack:
        current, ranges = stack.pop()
        if current in ['A', 'R']:
            if current == 'A':
                total += math.prod(high - low + 1 for low, high in ranges.values())
            continue

        stack = search(current, ranges, stack)
    return total

def smatcher(op, t, ab):
    a, b = ab
    match op:
        case '>':
            to = (t + 1, b)
            thru = (a, t)
            return t >= a, (to, thru)

        case '<':
            to = (a, t - 1)
            thru = (t, b)
            return t <= b, (to, thru)

if __name__ == '__main__':
    data = read_data('./data/2023/day19_input.txt', sep='\n\n', parser=parser)
    st = time()
    result = solve_part_one(data)
    et = time()
    print('PART ONE', result)
    print('TIME TAKEN', et - st)
    print()
    st = time()
    pt_result = solve_part_two(data)
    print('PART TWO', pt_result)
    print('TIME TAKEN', et - st)
    et = time()
