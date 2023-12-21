from random import randint


def radix_sort(lst):
    max_digits = max([len(str(x)) for x in lst])  # количество разрядов самого длинного числа
    base = 10  # основание системы счисления
    sorting_bins = [[] for _ in range(base)]  # промужеточный пустой массив
    # разделение чисел на положительные и отрицательные
    neg_nums = []
    pos_nums = []
    for num in lst:
        if num < 0:
            num *= -1  # убираем минус
            neg_nums.append(num)
        else:
            pos_nums.append(num)

    # отдельная сортировка отрицательных чисел
    for i in range(0, max_digits):  # цикл по рязрядам
        for x in neg_nums:
            digit = (x // base ** i) % base  # получаем цифру текущего разряда
            sorting_bins[digit].append(x)
        neg_nums = [x for order in sorting_bins for x in order]
        sorting_bins = [[] for _ in range(base)]
    neg_nums.reverse()  # срезом переворачиваем отрицательный список
    neg_nums = [-x for x in neg_nums]  # делаем все числа в списке отрицательными

    # отдельная сортировка положительных чисел
    for i in range(0, max_digits):  # цикл по рязрядам
        for x in pos_nums:
            digit = (x // base ** i) % base  # получаем цифру текущего разряда
            sorting_bins[digit].append(x)

        pos_nums = [x for order in sorting_bins for x in order]
        sorting_bins = [[] for _ in range(base)]
    lst = neg_nums + pos_nums
    return lst


# spisok = list(map(int, input().split()))
spisok = [randint(-10000, 10000) for i in range(10)]
print(spisok)
print(radix_sort(spisok))
