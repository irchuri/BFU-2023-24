arr1 = [1,5,67,89,2,33,4,12,13]
arr2 = [1,67,89,2.33,12,13]
counter = 0
for i in range(0, len(arr1)):
    for j in range(0, len(arr2)):
        if arr1[i] == arr2[j]:
            counter += 1
print(counter)