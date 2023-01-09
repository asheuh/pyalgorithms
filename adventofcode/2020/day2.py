import re
from read_file import read_data

def valid_password_1(policy):
    a, b, L, pw = policy
    return a <= pw.count(L) <= b

def valid_password_2(policy):
    a, b, L, pw = policy
    return (pw[a - 1] == L) ^ (pw[b - 1] == L) # XOR returns True if one is True and the other False else returns False

def part_one(policies):
    count = 0
    for policy in policies:
        if valid_password_1(policy):
            count += 1
    return count

def part_two(policies):
    count = 0

    for policy in policies:
        if valid_password_2(policy):
            count += 1
    return count
    

def parse_password_policy(line):
    policy, password = line.split(':')
    x, y, s = re.findall(r'[^-\s]+', policy)
    pw = re.sub(r"\s+", "", password)
    return (int(x), int(y), s, pw)

if __name__ == '__main__':
    filename = '../data/day2_input.txt'
    r = read_data(filename, parse_password_policy)
    result = part_one(r), part_two(r)
    print(result)
