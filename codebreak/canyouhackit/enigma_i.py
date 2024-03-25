# Funkschlüssel
# https://www.cryptomuseum.com/crypto/enigma/c/index.htm#std
# https://www.cryptomuseum.com/crypto/enigma/m3/
# https://en.wikipedia.org/wiki/Enigma_machine
import pprint
import string

from itertools import permutations
from copy import deepcopy
from time import sleep

def enigma_i(cipher, config):
    rotors = config.get('rotors', [1,2,3])
    plug_board = config.get('plug_board', {})
    all_rotor_perms = list(permutations(rotors, 3)) # All possible permuations; 3 of 5 rotors has 60 permutations
    ukw_c = 'FVPJIAOYEDRZXWGCTKUQSBNMHL' # Reflector
    ascii_upper = string.ascii_uppercase
    notch = config.get('notch', {})
    rotor_settings = config.get('rotor_settings', ('A', 'A', 'A'))
    copy_rotor_settings = deepcopy(rotor_settings)
    ring_settings = config.get('rings', ('A', 'A', 'A'))
    rotor_map = {
        1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
        2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
        3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
        4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
        5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
    }
    inverse = {
        1: "UWYGADFPVZBECKMTHXSLRINQOJ",
        2: "AJPCZWRLFBDKOTYUQGENHXMIVS",
        3: "TAGBPCSDQEUFVNZHYIXJWLRKOM",
        4: "HZWVARTNLGUPXQCEJMBSKDYOIF",
        5: "QCYLXWENFTZOSMVJUDKGIARPHB",
    }

    for rotor in all_rotor_perms:
        message = ''

        for c in cipher:
            i = 2
            rotor_settings = advance(rotor_settings, notch, ascii_upper, rotor)
            letter = plug_board.get(c, c)

            while i >= 0:
                r = rotor[i]
                step = ord(rotor_settings[i]) - ord(ring_settings[i])
                letter = apply_rotor(rotor_map[r][shift(letter, step)], step, ascii_upper)
                i -= 1

            # Reflector
            k = shift(letter)
            letter = ukw_c[k]

            # Reverse substitution(from left to right)
            i = 0
            while i < 3:
                r = rotor[i]
                step = ord(rotor_settings[i]) - ord(ring_settings[i])
                letter = apply_rotor(inverse[r][shift(letter, step)], step, ascii_upper)
                i += 1

            nletter = plug_board.get(letter, letter)
            message += nletter

        rotor_settings = copy_rotor_settings
        print(rotor, '==>', message)
        print('-' * (len(message) + 14))

def apply_rotor(char, offset, key):
    return key[shift(char, -offset)]

def shift(char, step=0):
    offset = 65 if char.isupper() else 97
    return (ord(char) - offset + step) % 26


def advance(s, notch, key, rotor):
    settings = list(s)
    if settings[1] == notch[rotor[1]]:
        settings[0] = key[shift(settings[0], 1)]
        settings[1] = key[shift(settings[1], 1)]

    if settings[2] == notch[rotor[2]]:
        settings[1] = key[shift(settings[1], 1)]

    settings[2] = key[shift(settings[2], 1)]
    return settings

def parse_plug(plug_board):
    pb = plug_board.split(' ')
    pb_map = {c[0]: c[1] for c in pb}
    pb_map.update({c[1]: c[0] for c in pb})
    return pb_map


if __name__ == '__main__':
    cipher = 'LYSIG WGMIY HLMQG YWOPI FNGIH QRDVF EILVS KDZGR DKCIX CIZIO PYGPJ VCUTT KVIDF EVAUO NHVLV DJVML OEZLD ABHCA BYCAK LVAHB SSOZQ DYSDY XFGPS JRTUL MPOL'
    config = {
        'rotors': [1, 2, 3, 4, 5], # 5 rotors
        'rings': ('K', 'Y', 'B'),
        'rotor_settings': ('L', 'I', 'F'),
        'notch': {1: 'Q', 2: 'E', 3: 'V', 4: 'J', 5: 'Z'},
        'plug_board': parse_plug('RU WS ZT XP BC VJ')
    }
    message = enigma_i(cipher.replace(" ", ""), config)
