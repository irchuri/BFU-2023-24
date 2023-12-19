from random import randint


def quick_Sort(lst: list[int]) -> list[int]:
    if len(lst) > 1:
        pivot = lst.pop(len(lst) // 2 + 1)
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in lst:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return quick_Sort(smlr_lst) + equal_lst + quick_Sort(grtr_lst)
    else:
        return lst



#spisok = [randint(-100, 100) for i in range(10)]
# spisok = list(map(int, input().split()))
spisok = ['11', '12', '-33']
print(spisok)
print(quick_Sort(spisok))
