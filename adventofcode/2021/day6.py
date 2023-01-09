import math
from time import sleep
from collections import Counter

from read_file import read_data

def part_one(timers, days=80):
    n_timers = timers
    number_of_fish = len(n_timers)
    counter = Counter(n_timers) # Keep a count of each timer
    ncount = 0

    def _process(timer):
        k = timer - 1
        if k < 0: # reset elapsed time
            k = 6 # 6 because lanternfish are assumed to spawn after 7 days and 0 is considered
        return k

    def _counter(list_tuple):
        """This function creates  new Counter and assigns to counter.
        This handles a case where the a doublicates for example n_t variable on line 34
        if n_t = [(2, 3), (2,4), (1,3), (1,5)] then counter will be {2: 7, 1: 8}
        """
        seen = {}
        for item in list_tuple:
            key, value = item
            try:
                seen[key] += value
            except Exception as e:
                seen[key] = value
        return seen

    for day in range(days):
        k, count = math.inf, 0
        n_t = [] # keep updated time and the count of that time i.e [(3, 14)] means 3 days appear 4 times

        if ncount:
            n_t.append((8, ncount))
            number_of_fish += ncount # old population plus new

        for key, value in counter.items():
            ncount = 0
            k = _process(key)
            n_t.append((k, value)) 

            if not k: # time has time has elapsed, so lanternfish can spawn new ones
                count += value

        ncount = count # ncount is the number of new lanternfish based of elapsed time
        counter = _counter(n_t) 
        print(f'After  {day + 1} day = {number_of_fish}')
    return number_of_fish

def part_two(timers):
    return part_one(timers, 1000)
    

if __name__ == '__main__':
    data = read_data('data/2021/day6_input.txt', parser=int, sep=',')
    result_p1 = part_one(data)
    result_p2 = part_two(data)
    print(result_p1, result_p2)
