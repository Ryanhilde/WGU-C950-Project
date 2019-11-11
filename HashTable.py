class HashTableEntry:

    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashMap:

    # Constructor
    # Space-time complexity is O(1)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # private getter to create a hash key
    # Space-time complexity is O(1)
    def _get_hash(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Insert a new package value into the hash table
    # Space-time complexity is O(N)
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Space-time complexity is O(N)
    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    # Grab a value from the hash table
    # Space-time complexity is O(N)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    # Remove a value from the hash table
    # runtime is O(N)
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
