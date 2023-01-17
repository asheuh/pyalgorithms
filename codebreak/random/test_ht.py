"""
Store key - value elements
Ht is dynamic in the sense that the size of the buckets changes with time when it gets full
    Note: buckets if where we store the key - value elements
We an initial size of the buckets, recommended to have as a prime numbers
Decide which hash functions:
    a hash function is a function that gets a value the generates a hash or unique identity of that value
if we the initial size call it n between 25 - 1000
Colitions:
    encountering same hash again
Handling a full bucket:
    load factor: is the threshhold we set to determine, default 0.75
    lf = k / n
    k : the number occopied in the buckets
"""

class HashTable:
    def __init__(self, size=13):
        self.size = size
        self.occupied = 0
        self.load_factor = 0.75
        self.buckets = [None] * self.size # (key, value)

    def _hash(self, key):
        return hash(key) % self.size

    def is_fulll(self):
        return (self.occupied / self.size) > self.load_factor

    def find_slot(self, key):
        index = self._hash(key)

        while self.buckets[index] and self.buckets[index][0] != key:
            index = index - 1

            if index < 0:
                index = self.size + index

        return index

    def double_hash(self):
        temp = self.buckets
        self.buckets = [None] * (self.size * 2)
        self.size = len(self.buckets)

        for item in temp:
            if item:
                key, value = item
                self.insert(key, value, 'new')

    def insert(self, key, value, dummy_key=None):
        index = self.find_slot(key)

        if self.is_fulll():
            self.double_hash()

        self.buckets[index] = (key, value)

        if dummy_key:
            self.occupied += 1

    def remove(self, key):
        i = self.find_slot(key)
        value = self.buckets[i]
        
        if not value:
            return

        self.buckets[i] = None
        j = i

        while True:
            i = i - 1

            if i < 0:
                i = self.size + i

            item = self.buckets[i]

            if not item:
                break

            k = self.find_slot(item[0])

            if (i <= k < j) or (k < j < i) or  (j < i <= k):
                continue

            self.buckets[j] = self.buckets[i]
            self.buckets[i] = None
            j = i

        self.occupied -= 1
        return value

    def get_value(self, key):
        index = self.find_slot(key)
        item = self.buckets[index]

        if not item:
            return

        return item[1]

if __name__ == '__main__':
    ht = HashTable()
    data = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7), ('I', 8), ('J', 9), ('K', 10), ('L', 11), ('M', 12)]

    for item in data:
        key, value = item
        ht.insert(key, value)

    print(ht.get_value('L'))
    print(ht.buckets)
    print(ht.remove('L'))
    print(ht.get_value('L'))
