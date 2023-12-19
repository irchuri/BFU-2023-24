class HashTable: 
    def __init__(self):
        self.MAX = 100
        self.hash_list = [[] for _ in range(self.MAX)]

    def get_hash(self, key: str) -> int:                # хеш-функция -- сумма ASCII-кодов символов в слове
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 100

    def __setitem__(self, key, val):  # добавление
        hash = self.get_hash(key)
        self.hash_list[hash].append((val, key))

    def __getitem__(self, key):  # вызов
        hash = self.get_hash(key)
        for element in self.hash_list[hash]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key):  # удаление
        hash = self.get_hash(key)
        for idx, element in enumerate(self.hash_list[hash]):
            if element[0] == key:
                del self.hash_list[hash][idx]


t = HashTable()
# t['march 1'] = 130  | добавить значение в таблицу
# del t['march 6']    | удалить значение из таблицы
# t['march 1']        | вызвать значение из таблицы
# t.arr               | просмотреть таблицу целиком
t['march 6'] = 120
t['march 6'] = 119
t['march 6'] = 130
print(t.hash_list)

