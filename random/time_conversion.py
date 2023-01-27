def time_conversion(s):
    # Write your code here
    to_add = 12
    if s.endswith('PM'):
        if s.startswith('12'):
            return s[:-2]
        else:
            a = s[:2]
            t = int(a) + 12
            return f'{t}{s[2:-2]}'
    else:
        if s.startswith('12'):
            return f'00:{s[3:-2]}'
        return s[:-2]

if __name__ == '__main__':
    to_con = '03:59:00PM'
    t = time_conversion(to_con)
    print(t)
