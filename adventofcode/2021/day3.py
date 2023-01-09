# Binary Siagnostic
from time import sleep

from read_file import read_data

def set_bit_counter(d_report):
    d_report = list(d_report)
    sbc = {i: 0 for i in range(len(d_report[0]))}

    for dr in d_report:
        for i, bit in enumerate(dr):
            f = int(bit)
            if f & 1:
                sbc[i] += 1
    return sbc

def part_one(d_report):
    g_rate = ''
    n = len(d_report)
    sbc = set_bit_counter(d_report)

    for k, v in sbc.items():
        clear_bits_count = n - v

        if clear_bits_count > v:
            g_rate += '0'
        else:
            g_rate += '1'
    g = int(g_rate, base=2)
    # (2 ** len(g_rate) - 1) is sames 11111 if len(g_rate) if 5
    # so 01010 ^ 11111 = 10101 -> XOR
    e = g ^ (2 ** len(g_rate) - 1) 
    return g * e


def find_ratings(d_report, xbit, ybit, key: str='oxygen'):
    """
    Finding the oxygen generator and CO2 scrubber rating
    The '>', '<', and '=' on line 63, 65 and 67 respectively, represents the
    identifier for whether to use ybit for '=' when the bit count is the same 
    params:
        d_report(list): diagnostic report
        xbit(str): 0 or 1 bit depending on whether we are finding oxygen or CO2
        ybit(str): 0 or 1 bit depending on whether we are finding oxygen or CO2
        key(str): Oxygen or CO2, describes what we are finding
    return:
        rating in binary string
    """
    n = len(d_report[0])
    kept = len(d_report)

    def _set_bit_counter(d_report, i):
        check = {i: 0}
        for dr in d_report:
            f = int(dr[i])
            if f & 1: # count only set bits i.e '1'
                check[i] += 1
        return check

    for i in range(n):
        v = _set_bit_counter(d_report, i)[i]
        clear_bits_count = len(d_report) - v

        if clear_bits_count > v:
            d_report = set_kept_batch(d_report, i, '>', xbit)
        elif clear_bits_count < v:
            d_report = set_kept_batch(d_report, i, '<', ybit)
        else:
            d_report = set_kept_batch(d_report, i, '=', ybit) # if the bits count is equal, ybit = 0 for CO2 and 1 for exygen
        kept = len(d_report)

        if kept == 1: # stop searching when one is remaining; this is our result 
            break
    
    return d_report[0] # rating

def part_two(d_report):
    ogr = find_ratings(d_report, '0', '1') # oxygen generator rating
    co2sr = find_ratings(d_report, '1', '0', 'co2') # CO2 scrubber rating
    lsr = int(ogr, 2) * int(co2sr, 2) # life support rating: ogr * co2sr
    return lsr

def set_kept_batch(d_report, i, sign, bit):
    """Search and destroy the unwanted"""
    drs = []
    for dr in d_report:
        if sign == '=' or sign == '<':
            if dr[i] == bit:
                drs.append(dr)
            continue

        if dr[i] == bit:
            drs.append(dr)
    return drs
                

if __name__ == '__main__':
    data = read_data('../data/2021/day3_input.txt')
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p2)
