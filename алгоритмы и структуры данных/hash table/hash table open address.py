class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None] * self.MAX

    def get_hash(self, key: str) -> int:
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, val):
        hash = self.get_hash(key)

        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                break  # если ключ найден, пихаем в следующий свободный слот
            hash = (hash + 1) % self.MAX

        self.arr[hash] = (key, val)

    def __getitem__(self, key):
        hash = self.get_hash(key)
        initial_hash = hash

        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                return self.arr[hash][1]
            hash = (hash + 1) % self.MAX

            # если ничего не нашли
            if hash == initial_hash:
                break

        raise KeyError(key)

    def __delitem__(self, key):
        hash = self.get_hash(key)

        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                self.arr[hash] = None
                return
            hash = (hash + 1) % self.MAX

        raise KeyError(key)


t = HashTable()
t['march 1'] = 130
del t['march 1']
t['march 6'] = 120
print(t['march 6'])
