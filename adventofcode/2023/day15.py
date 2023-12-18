import re
import string

from read_file import read_data
from python.pyalgorithms.datastructure.hashbased.hashtable import HashTable


class HashMap(HashTable):
    def __init__(self, size=13):
        super().__init__(size)

    def _hash(self, key):
        def hash_algorithm(s):
            if isinstance(s, int):
                return s

            current = 0
            n = len(s)
            i = 0
            while i < n:
                k = ord(s[i])
                current = ((current + k) * 17) % 256
                i += 1
            return current
        return hash_algorithm(key)

    def insert(self, key, value, id='new'):
        box_number = self._hash(key)
        self.buckets[box_number] = (key, (box_number, value))

    def get(self, key):
        return self.buckets[self._hash(key)]

def parser(line):
    return re.findall(r'(\w+)(=|-)(\d)?', line)[0]

def find_slot(box_slots, key):
    i = len(box_slots) - 1
    found = False
    while i >= 0 and box_slots:
        if box_slots[i][0] == key:
            found = True
            return (found, i)
        i -= 1
    return (found, i)

def create_hash_map(steps):
    hm = HashMap(256) # 256 boxex; 0..255
    for step in steps:
        label, op, fl = step
        # Get the box if exists
        box = hm.get(label)
        box_number = hm._hash(label)
        new_box = []
        if box:
            _, (_, new_box) = box

        found, index = find_slot(new_box, label)
        if found:
            if op == '-': # Delete
                new_box.pop(index)

            if op == '=':
                new_box[index] = (label, int(fl))
        else:
            if op == '=':
                new_box.append((label, int(fl)))
            else:
                continue

        # add boxes
        hm.insert(label, new_box)
    return hm

def solve_part_one(steps):
    hm = HashMap()
    def hashing(s):
        for i in s:
            c = ''.join(i)
            yield hm._hash(c)
    return sum(hashing(steps))

def solve_part_two(steps):
    hm = create_hash_map(steps)
    total = 0
    for i, b in enumerate(hm.buckets):
        if not b:
            continue

        label, (box_number, box) = b
        total += sum([
            (box_number + 1) * (x + 1) * y
            for x, (_, y) in enumerate(box)
        ])
    return total

if __name__ == '__main__':
    data = read_data('./data/2023/day15_input.txt', parser=parser, sep=',')
    result = solve_part_one(data)
    pt_result = solve_part_two(data)
    print('PART ONE ====>', result)
    print('PART TWO ====>', pt_result)
