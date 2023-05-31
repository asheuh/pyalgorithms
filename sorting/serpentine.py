from time import sleep
import re
import natsort

from collections import OrderedDict

data = [
    '1A A 01 01',
    '1A A 01 03',
    '1A A 01 05',
    '1A B 02 12',
    '1D K 03 09',
    '1B D 01 02',
    '1D K 04 08',
    '1A C 02 03',
    '1A C 02 05',
    '1A C 04 03',
    '1A C 02 08',
    '1B F 05 03',
    '1B F 06 09',
    '1B E 07 04',
    '1B E 05 05',
    '1B E 07 09',
    '1B D 07 05',
    '1B D 01 09',
    '1B D 07 05',
    '1D L 05 07',
    '1D L 02 06',
    '1A A 02 09',
    '1C I 01 03',
    '1C I 08 03',
    '1A A 02 04',
    '1A A 02 05',
    '1A A 02 02',
    '1A B 03 03',
    '1A B 03 06',
    '1A B 03 07',
    '1A B 03 03',
    '1C G 03 08',
    '1A A 04 05',
    '1C G 02 03',
    '1C H 01 05',
    '1C H 07 06',
    '1D J 04 04',
    '1D J 05 06',
]


data = [
    '2A A 01 04',
    '2B B 01 05',
    '1A A 01 03',
    '3B A 01 03',
    '6A A 01 05',
    '3A B 03 04',
    '9B D 01 05',
    '1B B 01 02',
    '5B C 01 03',
    '10A A 01 02',
    '7B F 01 02',
    '12A E 01 05',
    '8A E 01 02',
    '4B A 01 03',
    '4A C 01 03',
    '11B A 01 04',
]

data = [
    'BA A 01 04',
    'BB B 01 05',
    'AA A 01 03',
    'CB A 01 03',
    'FA A 01 05',
    'CA B 03 04',
    'IB D 01 05',
    'AB B 01 02',
    'EB C 01 03',
    'JA A 01 02',
    'GB F 01 02',
    'LA E 01 05',
    'HA E 01 02',
    'DB A 01 03',
    'DA C 01 03',
    'KB A 01 04',
]

data2 = [
    '1A A 01 04',
    '1A B 01 05',
    '2A A 01 03',
    '2A A 01 03',
    '5A A 01 05',
    '5A B 03 04',
    '8A D 01 05',
    '8A B 01 02',
    '7A C 01 03',
    '7A A 01 02',
    '6A F 01 02',
    '6A E 01 05',
    '4A E 01 02',
    '4A A 01 03',
    '3A C 01 03',
    '3A A 01 04',
]

data = [
    '1A A 01 04',
    '1A B 01 05',
    '1A A 01 03',
    '1A A 01 03',
    '1A A 01 05',
    '1A B 03 04',
    '1A D 01 05',
    '1A B 01 02',
    '1A C 01 03',
    '1A A 01 02',
    '1A F 01 02',
    '1A E 01 05',
    '1A E 01 02',
    '1A A 01 03',
    '1A C 01 03',
    '1A A 01 04',
]

import pprint

def serpentine_sort_algorithm(locations, levels=[2]):
    indices = [value-1 for value in levels]
    locations = natsort.natsorted(locations) # We first sort normally: ascending order
    results = []

    def left_right(second_group):
        def find_break_index(i, num_str, group, sections):
            j = i + 1
            while j < n:
                item, = sections[j]
                if item.startswith(num_str):
                    group.append(sections[j])
                    j += 1
                else: break
            i = j
            return i, group

        sections = list(second_group.keys()) 
        serps = []
        sorted_serpentines = []
        i = 0
        n = len(second_group)
        if not sections: return []

        group = []
        seen = set()
        while i < n:
            item, = sections[i]
            group.append(sections[i])
            digits = re.findall(r'\d+', item)
            if digits:
                num_str = digits[0] # We are interested in the first
                seen.add(num_str)
                i, group = find_break_index(i, num_str, group, sections)
            else: # Onlyt characters
                num_str = item[0] # We are interested in the first
                seen.add(num_str)
                i, group = find_break_index(i, num_str, group, sections)
                
            if len(seen) == 3: # Reset data structures
                serps.append(group)
                group = []
                seen.clear()

        if group and not serps:
            serps.append(group)

        for reverse, g in [(True, _group) if i & 1 else (False, _group) for i, _group in enumerate(serps)]:
            sorted_serpentines.extend(natsort.natsorted(g, reverse=reverse))
        return sorted_serpentines

    def group_levels(locs, index):
        groups = OrderedDict()
        for location in locs:
            key = tuple(location[:index])
            value = location[index:]
            if key not in groups:
                groups[key] = [value]
            else:
                groups[key].append(value)
        return groups

    def sorter(index):
        picks = []
        groups = group_levels(locations, index)
        serpentines = [True if i & 1 else False for i in range(len(groups.keys()))] # Parse serpentine sort structure
        pprint.pprint(groups)
        for index, key in enumerate(groups.keys()):
            value = groups[key]
            value = natsort.natsorted(value, key=lambda value: value[0], reverse=serpentines[index]) # Sort in serpentine order
            if len(serpentines) == 1:
                # arrange from left to right if serpentine structure is not set
                # which means, either level 1 or 2 is amongst the selected levels
                second_group = group_levels(value, index + 1)
                sorted_second_group = left_right(second_group)
                value = []
                for sg in sorted_second_group:
                    x, = sg
                    val = second_group[sg]
                    sg_value = [[x, *v] for v in val]
                    value.extend(sg_value)
            picks.extend([list(key) + item for item in value])
        return picks

    for index in indices:
        results = sorter(index)
        locations = results
    return results

results = serpentine_sort_algorithm([item.split(' ') for item in data])
pprint.pprint(results)

