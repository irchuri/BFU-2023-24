#list_old = list(map(int, input().split()))

list_old = [1,21,25,3,13,41,55,45,67,76,6,7,4,5,34,423,213]
list_new = []
for i in range(1, len(list_old)):
    if list_old[i] > list_old[i-1]:
        list_new.append(list_old[i])

print(*list_new)