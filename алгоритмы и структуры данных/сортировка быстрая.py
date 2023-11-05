from random import randint


def quickSort(array):
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst)
    else:
        return array


spisok = [randint(-100, 100) for i in range(10)]
# spisok = list(map(int, input().split()))

print(spisok)
print(quickSort(spisok))
