from random import randint, choice


def Quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = choice(nums)  # выбор псевдослучайного пивота
        # разделение на три списка: меньше пивота, больше пивота, равные пивоту
        lesser_pivot = [n for n in nums if n < pivot]
        greater_pivot = [n for n in nums if n > pivot]
        equal_pivot = [pivot] * nums.count(pivot)

        return Quick_sort(lesser_pivot) + equal_pivot + Quick_sort(greater_pivot)


# spisok = list(map(int, input().split()))
spisok = [randint(-100, 100) for i in range(10)]
print(spisok)
print(Quick_sort(spisok))
