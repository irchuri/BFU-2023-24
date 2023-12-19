from random import randint


def quick_Sort(unsorted_numbers: list[int]) -> list[int]:
    if len(unsorted_numbers) > 1:
        pivot = unsorted_numbers.pop(len(unsorted_numbers) // 2 + 1)
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in unsorted_numbers:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return quick_Sort(smlr_lst) + equal_lst + quick_Sort(grtr_lst)
    else:
        return unsorted_numbers



#spisok = [randint(-100, 100) for i in range(10)]
# spisok = list(map(int, input().split()))
spisok = ['11', '12', '-33']
print(spisok)
print(quick_Sort(spisok))
