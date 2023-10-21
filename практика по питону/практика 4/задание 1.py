#arr = list(map(int, input().split()))
arr = [1,5,3,6,4,34,5,13,4,54,5,4,3,5,45,23,4,256]
ind_min = arr.index(min(arr))
ind_max = arr.index(max(arr))
arr[ind_min], arr[ind_max] = arr[ind_max], arr[ind_min]
print(*arr)