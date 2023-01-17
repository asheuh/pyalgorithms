class HashTable:
    def __init__(self, size=13):
        self.buckets = [None] * size
        self.size_occupied = 0
        self.load_factor = 0.75 # default for java 10
        self.size = len(self.buckets)

    def size(self):
        return len(self.buckets)

    def is_full(self):
        """Load factor = n / k
        where n: number of occupied slots in the buckets
              k: number of slots in the buckets
        """
        return (self.size_occupied / self.size) > self.load_factor

    def _hash(self, key):
        return hash(key) % self.size

    def find_slot(self, key):
        """To solve collision using open addressing or closed hashing
        We find the slot the has either a key same as the one we are
        looking for or an empty slot in which we insert there
        """
        
        index = self._hash(key)

        while self.buckets[index] and self.buckets[index][0] != key:
            index = index - 1
            if index < 0:
                index = index + self.size
        return index

    def alt_rehashing(self):
        """Alternative to all-at-once rehashing"""
        pass


    def double_hash(self):
        """To double the size of buckets if load factor is exceeded"""
        temp = self.buckets
        size = self.size
        self.buckets = [None] * (self.size * 2)
        self.size = len(self.buckets)

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
                i = i + self.size

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

if __name__ == '__main__':
    data = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6),
            ('G', 7), ('H', 8), ('I', 9), ('J', 10), ('K', 11), ('L', 12),
            ('M', 13), ('N', 14), ('O', 15), ('P', 16), ('Q', 17), ('R', 18),
            ('S', 19), ('T', 20), ('V', 21), ('U', 22), ('W', 23), ('X', 24), ('Y', 25), ('Z', 26)]


    ht = HashTable()

    for item in data:
        key, value = item
        ht.insert(key, value)

    print('ADDED', ht.buckets)

    for item in data:
        key, _ = item
        ht.remove(key)

    print('REMOVED', ht.buckets)
    va = ht.get('A')
    print(va)
    print(ht.size_occupied)
    ht.insert('Brian', '28')
    bm = ht.get('BrIaN')
    print(ht.buckets)
    print('Value', bm)
    print(ht.size_occupied)

