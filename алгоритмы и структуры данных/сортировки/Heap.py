from random import randint

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

spisok = [randint(-100, 100) for i in range(10)]
#spisok = list(map(int, input().split()))
print(spisok)


n = len(spisok)
for i in range(n // 2, -1, -1):
    heapify(spisok, n, i)
for i in range(n-1, 0, -1):
    spisok[i], spisok[0] = spisok[0], spisok[i]
    heapify(spisok, i, 0)
print(spisok)