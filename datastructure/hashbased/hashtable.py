"""
Hash Table data structure
"""


class HashTable:
    def __init__(self, size=13):
        self.buckets = [None] * size
        self.size_occupied = 0
        self.load_factor = 0.75 # default for java 10

    def size(self):
        return len(self.buckets)

    def is_full(self):
        """Load factor = n / k
        where n: number of occupied slots in the buckets
              k: number of slots in the buckets
        """
        return (self.size_occupied / self.size()) > self.load_factor

    def _hash(self, key):
        return hash(key) % self.size()

    def find_slot(self, key):
        """To solve collision using open addressing or closed hashing
        We find the slot that has either a key same as the one we are
        looking for or an empty slot in which we insert there
        """
        
        index = self._hash(key)

        while self.buckets[index] is not None and self.buckets[index][0] != key:
            index = index - 1
            if index < 0:
                index = index + self.size()
        return index

    def alt_rehashing(self):
        """Alternative to all-at-once rehashing"""
        pass


    def double_hash(self):
        """To double the size of buckets if load factor is exceeded"""
        temp = self.buckets
        size = self.size()
        self.buckets = [None] * (self.size() * 2)

        for i in range(size):
            item = temp[i]

            if item:
                key, value = item
                self.insert(key, value, 'old')

    def insert(self, key, value, id='new'):
        key = key.lower()
        if self.is_full():
            self.double_hash()

        index = self.find_slot(key) 
        self.buckets[index] = (key, value)

        if id == 'new':
            self.size_occupied += 1

    def get(self, key):
        key = key.lower()
        index = self.find_slot(key)

        if not self.buckets[index]:
            return
        return self.buckets[index][1]

    def remove(self, key):
        key = key.lower()
        i = self.find_slot(key)

        if not self.buckets[i]:
            return

        self.buckets[i] = None
        j = i

        while True:
            i = i - 1

            if i < 0:
                i = i + self.size()

            item = self.buckets[i]

            if not item:
                break

            r = self.find_slot(item[0])

            if (i <= r < j) or (r < j < i) or (j < i <= r): # find if r is cyclically between i and j
                continue

            self.buckets[j] = self.buckets[i]
            self.buckets[i] = None
            j = i

        self.size_occupied -= 1

