import re

from read_file import read_data
from collections import defaultdict

def part_one(passports):
    count_valid = 0

    for passport in passports:
        if valid_passport(passport):
            count_valid += 1
    return count_valid

def valid_passport(passport):
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    keys = set(passport.keys())

    if not (fields ^ keys):
        return True

    if not ((fields ^ keys) ^ {'cid'}):
        return True

    return False

def valid_passport_pt(passport):
    '''Passport rules
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''
    valid = []
    for key, value in passport.items():
        if key == 'byr':
            valid.append(1920 <= int(value) <= 2002)
        
        if key == 'iyr':
            valid.append(2010 <= int(value) <= 2020)

        if key == 'eyr':
            valid.append(2020 <= int(value) <= 2030)

        if key == 'hgt':
            last_two = value[-2:]
            if last_two in ['cm', 'in']:
                if last_two == 'cm':
                    digit = value[:-2]
                    valid.append(150 <= int(digit) <= 193)
                else:
                    digit = value[:-2]
                    valid.append(59 <= int(digit) <= 76)
            else:
                valid.append(False)

        if key == 'hcl':
            if re.match('#[0-9a-f]{6}$', value):
                valid.append(True)
            else:
                valid.append(False)

        if key == 'ecl':
            valid.append(value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'})

        if key == 'pid':
            valid.append(len(value) == 9 and value.isdigit())

    return all(valid)

def better_version_of_valid_passport_pt(passport):
    valid = []
    for key, value in passport.items():
        if key == 'byr':
            valid.append(1920 <= int(value) <= 2002)
        
        if key == 'iyr':
            valid.append(2010 <= int(value) <= 2020)

        if key == 'eyr':
            valid.append(2020 <= int(value) <= 2030)

        if key == 'hgt':
            check = ((value.endswith('cm') and 150 <= int(value[:-2]) <= 193) 
                    or (value.endswith('in') and 59 <= int(value[:-2]) <= 76))
            valid.append(check) 

        if key == 'hcl':
            valid.append(re.match('#[0-9a-f]{6}$', value))

        if key == 'ecl':
            valid.append(re.match('(amb|blu|brn|gry|grn|hzl|oth)$', value))

        if key == 'pid':
            valid.append(re.match('[0-9]{9}$', value))
    return all(valid)

def part_two(passports):
    count_valid = 0
    for passport in passports:
        if valid_passport(passport) and better_version_of_valid_passport_pt(passport):
            count_valid += 1
    return count_valid

def process_batch_data(data):
    d = defaultdict(list)
    a = 1
    passports = []

    for item in data:
        line = item.split(' ')
        d[a].extend(line)

        if item == '':
            a += 1

    for i in range(len(d) + 1):
        dict_data = {i.split(':')[0]: i.split(':')[1] for i in d[i] if i}
        passports.append(dict_data)

    return passports



if __name__ == '__main__':
    filename = "../data/day4_input.txt"
    r = read_data(filename)
    rs = process_batch_data(r)
    result = part_one(rs), part_two(rs)
    print(result)

