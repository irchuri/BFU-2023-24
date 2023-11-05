import  random
def selection_sort(spisok):
    for i in range(0, len(spisok) - 1):
        smallest = i
        for j in range(i + 1, len(spisok)):
            if spisok[j] < spisok[smallest]:
                smallest = j
        spisok[i], spisok[smallest] = spisok[smallest], spisok[i]
        print(spisok)


#spisok = list(map(int, input().split()))
spisok = [random.randint(-100, 100) for i in range(10)]
selection_sort(spisok)
print(spisok)