import math, pprint, re

from collections import defaultdict
from time import sleep
from functools import reduce

from read_file import read_data


HEX_BIN_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

PADDING = {
    '0': '0000',
    '1': '000',
    '2': '00',
    '3': '00',
    '4': '0',
    '5': '0',
    '6': '0',
    '7': '0',
}


def part_one(hd: list, is_part2=False):
    def hard_reset(istlset, tl, isnspset, nsp):
        if istlset and tl <= 0:
            istl_set = False
            tl = 0
        if isnspset and nsp <= 0:
            isnspset = False
            nsp = 0
        return istlset, isnspset, nsp, tl

    def compute(result, popped, mkey):
        output = result[-popped:]
        out = calculation(output, mkey)
        return [*result[:-popped], out]

    hexadecimal = hd[0]
    packet = hex_to_bin(hexadecimal)
    istlset = isnspset = False
    literal_value = 4
    tl = nsp = total_version_number = 0
    stack = [packet]
    mains, values, result = [], [], []
    mode = (None, math.inf, math.inf)
    remaining = 0 
    popped = 0

    while stack:
        current = stack.pop()
        V_decimal, T_decimal = (int(current[:3], 2), int(current[3:6], 2)) # V --> packet version, T --> packet type ID
        rest = current[6:]
        a = 0
        # 110 000 1 00000110101 111 001 0 000000010100000 000 100 101111101110011101101001000011 101 110 1 00000000010 110 000 1 00000000011 000 100 00110 011 100 01101 100 100 00111 010 000 0 000000000100001 101 100 01010 111 100 00011 011 100 00101 011 011 1 00000000101 000 100 1101001000 110 100 1111010000110101100100000 110 100 110001111111100110001110100100 100 100 1111110000111101110001011 111 100 01101 011 010 1 00000000100 011 100 01001 110 100 101001101110100110111011010110110111001101111011100101100111100110010100010101100010000000001001011000111000000000010000001010011100010011011001110001001001100111001001000101010001000000000110101000010011001110011001010000001000111101000000000100111001101010001101011110100100010100101111110111010001001110010000000010011010111111000000000110101010100000000000001000011101000010100110000101011100010111010001000000000110001000101011010000110011100011001101001101011101110000000010100100000000010010110101001101001110101110000000000010010100110010111100100011010010010100011010010001000000000111000010000000000100001110100010101101000100000010000010100001000000000010000110110000011000100011000101000100101000100000000001000010111000011000110001011101100010001110011000000000100111001111010000101101100101110010101100000000010010100110001100111010011000111001100011001110100110000100100000000011100110001001001111110000011001010000000001001000110100100011000111101111111001110001111000001001110010110100101101001101010010100000000001100100001111100010000000001000000101100101000001111010010010001101001001000100101000100110010110011000100000001100001111110110000000101110001000001000000010101101101001110000000000110100000000001001100111010000000000100011101011000100000000001100001100000000001110001100000000001100010100000000001001011100000000001100011000000001010110101101000000000100101110010101000000000010110001000000000010100001000000000011100011000000000010100011000000000011100111000000000010000110000000000010101100100101011000101001010011100000000100100100111111000100011110100000111111001000100010101100111010010101001110000000001011110010100100110110110010010110010111010011000000000101101011000000000101111001001010100010101001001010110001101001110010001100100011001010010010010110001001011011100100101011000111011001100000000101010100111110111001010010100001111011001111001001001100111000110100010011110001110100010000000010011101110000100000000011110100000110001000010110110000101010000100000000011101100000100101000100110110000010000000000000000010000101010001011100100011111011000111101100100000000001100001011001010001011101100110000110100010010001001100001001011111001010101110010000000000010000110100111000001011001010000000001110010001110011100111101101111101111010001010010011010111111110101101101000100000000010010100100101110100010111100101000010100110010001100110011110000100000000011001000111001001010011110011100101001110101000000000010111110010011100111101101011100001010111001110101011001001000000000010000001010010001000000001001011101110000001000000001010101001110110000000001000100010000000001111110000010011100010010001000100100000000000000001000011001000111011110001011100100010001111001010011100100101100011000110001010001011101010000000001000001010010011000110011000010101101010110100110010100011000101001110010100111101011001100111100111011000010010011110001001101111000001110110110000000000001011100100001010010010000000001101110001100110010011111010100000000010010000101001001110001101011101010001011111001001001110001101011101010001011110100001000000001011101001110110000111111111111110000011011001110010010111111011010010101011110110110000001101001010000001111100101100101011110010001011110110000000000001010011001100100111110111101101110001000010011000110111111101000000100101101000110000010110010010000000001100100011111000000000011111000010010100101010110111010011010111001011111101100001110000110111100110000101101010001011101001100000000010111110000000000011111010110010101100101001101000101100100111000010100111111100000001111100101011100010100110111111010110000000110101000000000100111000000101010010110001001100010000000001100100111100101000111100011100000000001111100111001111110001110111010111101000011111001111010100101010110111000110000000001010111000000000001111100011001010010110010111011001100010100101001010010110100110101111010010001111100111100000110000000001011110011100100011111110001001011101010000000001010010011100110001000110110001001111001011111011100101111011111101011010011000101110110011100110000000001000110100000000011001101010001000000000110101000101001110001101100100010001110001000000000110101000011100110000010011100000101101001110001100100001000000000101000000110011101001110111100000000000101010110100111011000001001000100111011000001001010100001000101001011111000110001000011010010001111000110000010001111000001100000000010100110100000000010110000000000000010000111110001000000100010011101000101011100000000000001000010001000011111110000100111100011100111001101011001111110001001100110000000001010011000000000001000000011001001001001011100100100100100010011001110100011100000010000000010010110011101101100001110110011010101101000111100100111000011101100101000100100000100110101010011111110011101111000100101001110111110110100110110001010001100110111001111100101101011101010001000000000000000101111110000110101011100000000011111100100101011110001001010111001011111000111110001011110011111111011110000000010100101010111100

        if T_decimal == literal_value:
            # if literal_value, we consider the rest of bits in groups of 5
            # if a group starts with a prefix of a 0, we stop reading, otherwise continue
            i = 0
            while rest[i] != '0':
                i += 5
            i += 5 # the loop will stop at the first index of the group
            sub_packs = int(rest[:i], 2)
            metamodes = {
                '0': (i + 6),
                '1': 1,
                None: 1
            }
            print(mains, sub_packs, values, result)

            if mains:
                modex, modey, N = mode
                lti, key, z, count = mains.pop()
                metavalue = metamodes[lti]
                print(count, metavalue, modey)

                if count > 0:
                    count -= metavalue
                    try:
                        res = values.pop()
                        print('VALUE', res, key)
                        if res[0] != key:
                            result.append(res)
                            values.append((key, sub_packs))
                        else:
                            new_value = calculation([res, (key, sub_packs)], key)
                            values.append(new_value)
                    except Exception as e:
                        values.append((key, sub_packs))

                    mains.append((lti, key, z, count))
                    print('WTF!!', count)

                    if count == 0:
                        _M, _k, E, sn = mains.pop()
                        popped += 1
                        print('GG', mains, values, popped, (_M, _k, E, sn))
                        
                        if mains:
                            k, v = values.pop()
                            B = 0
                            if _M == '1':
                                B = (N * modey)
                            else:
                                print('TUKOHAPA')
                                B = (N - sn)

                            result.append((k, v))
                            xyz = (E + B)
                            moc, p, e, c = mains.pop()
                            print('RESULT', result)
                            print('PREV', p, e, N, modey, mains, c)
                            if moc == '1':
                                c -= metamodes[moc]
                                e += xyz
                            else:
                                print('KKKKKK', N , E, B, xyz, (E + B + xyz), c)
                                c -= xyz
                                e += xyz

                            new_popped = popped
                            is_whiled = False
                            while c == 0 and mains:
                                if p == '1':
                                    print('HAHAHAHAHAHAHA', new_popped)
                                    new_popped += 1
                                print('HEWEWWEWEW', p)
                                result = compute(result, new_popped, p)
                                print('RRRRR', result)
                                tempe = e
                                tempc = c
                                moc, p, e, c = mains.pop()
                                if moc == '1':
                                    c -= metamodes[moc]
                                else:
                                    c -= tempe
                                e = tempe
                                new_popped = 1
                                popped = new_popped
                                is_whiled = True

                            if not mains and not is_whiled:
                                result = compute(result, popped, _k)
                            mains.append((moc, p, e, c))
                        print('POP', mains, values, result)
                        sleep(0.3)

            print(values, mains, result)
            rest = rest[i:]
            total_version_number += V_decimal
            if nsp > 0:
                nsp -= 1

            if tl > 0:
                tl -= (i + 6)
            istlset, isnspset, nsp, tl = hard_reset(istlset, tl, isnspset, nsp)
        else:
            # means we are dealing with an operator. The packet contains one or more sub-packets
            # to perform calculations on
            modes = {
                '0': 15,
                '1': 11
            }
            LTI = rest[0] # represents the Length type ID
            next_bits = modes[LTI]
            bits = rest[1: next_bits + 1]
            rem = rest[next_bits + 1:]
            num = int(bits, 2) # total length in bits or number of sub-packets
            if nsp > 0:
                nsp -= 1
            
            if tl > 0:
                tl -= (num + 7)
            istlset, isnspset, nsp, tl = hard_reset(istlset, tl, isnspset, nsp)
            nbt7 = (next_bits + 7)
            if mains:
                _i = len(mains) - 1
                print(mains, 'BEFORE', _i)
                if _i == 0:
                    popped = 0

                tempnbt7 = nbt7
                while _i >= 2: 
                    M, L, EX, C = mains[_i]
                    print('ONE', M, L, EX, C)
                    if M == '0':
                        C -= nbt7 
                        nbt7 = 0
                        print('KKEKKEKEKEKEKKE', C)
                        if C <= 0:
                            popped += 1
                            result = compute(result, popped, L)
                            print('WHAT WHAT WHAT!', result)
                            _ = mains.pop(_i)
                            _i -= 1
                            M, L, EX, C = mains[_i]
                            mains[_i] = (M, L, EX, C)
                            if M == '1':
                                C -= metamodes[M]
                            nbt7 = tempnbt7
                            popped = 0
                            break
                    mains[_i] = (M, L, EX, C)
                    _i -= 1
                    nbt7 = tempnbt7
                else:
                    M, L, EX, C = mains[_i]
                    print('ONE', M, L, EX, C)
                    if M == '0':
                        C -= nbt7 
                        nbt7 = 0
                        print('KKEKKEKEKEKEKKE', C)
                        if C <= 0:
                            popped += 1
                            result = compute(result, popped, L)
                            print('WHAT WHAT WHAT!', result)
                            _ = mains.pop(_i)
                            _i -= 1
                            M, L, EX, C = mains[_i]
                            mains[_i] = (M, L, EX, C)
                            if M == '1':
                                C -= metamodes[M]
                            popped = 0
                    mains[_i] = (M, L, EX, C)
                    print(mains, 'AFTER')

            if LTI == '0':
                tl = num
                tess = num
                istlset = True
            else:
                nsp = num
                tess = num
                isnspset = True
            rest = rem
            main = f'{T_decimal}'
            print('HERE MF', (LTI, main, nbt7, num))
            mains.append((LTI, main, nbt7, num))
            mode = (LTI, len(bits), num)
            total_version_number += V_decimal 

        if not set(rest) ^ set('0') or not rest:
            break
        stack.append(rest)

    if is_part2:
        _, _main_key, _, _ = mains[0]
        out = calculation(result, _main_key)
        print()
        print('VALUES --->', values)
        print()
        print('MAINS --->', mains)
        print()
        print('RESULT --->', result, len(result))
        print()
        print('OUT --->', out)
        return out
    return total_version_number


def calculation(sequence, key5):
    sequence = [i[1] for i in sequence]
    if len(sequence) == 1:
        return key5, sequence[-1]
    return {
        '0': (key5, reduce(lambda x, y: x + y, sequence)),
        '1': (key5, reduce(lambda x, y: x * y, sequence)),
        '2': (key5, min(sequence)),
        '3': (key5, max(sequence)),
        '5': (key5, 1 if sequence[0] > sequence[1] else 0),
        '6': (key5, 1 if sequence[0] < sequence[1] else 0),
        '7': (key5, 1 if sequence[0] == sequence[1] else 0) 
    }[key5]


def hex_to_bin(hex_value):
    """Convert hexadecimal to binary representation"""
    first_dig = hex_value[0]
    pad = ''
    if first_dig in PADDING:
        pad = PADDING[first_dig]
    return pad + bin(int(hex_value, 16))[2:]


def part_two(hexadecimal):
    return part_one(hexadecimal, True)


if __name__ == '__main__':
    data = read_data('data/2021/day16_input.txt')
#     result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p2)
