class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key: str) -> int:  # хеш-функция -- сумма ASCII-кодов символов в слове
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 100

    def __setitem__(self, key, val):  # добавление
        hash = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hash]):
            if len(element) > 0 and element[0] == key:  # проверка, есть ли в таблице какой-то ключ на заданной позиции
                found = True                             # если есть, вставляем кортеж ключ-значение во вложенный список
                break
        if not found:                                    # если нет то всё ок и просто вставляем как обычно
            self.arr[hash].append((key, val))
        else:
            self.arr[hash][idx] = (key, val)

    def __getitem__(self, key):  # вызов
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key):  # удаление
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][idx]


t = HashTable()
# t['march 1'] = 130  | добавить значение в таблицу
# del t['march 6']    | удалить значение из таблицы
# t['march 1']        | вызвать значение из таблицы
# t.arr               | просмотреть таблицу целиком
t['march 6'] = 120
