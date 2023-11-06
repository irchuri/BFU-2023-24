nums = list()

with open ('file2.txt') as f:
    for line in f:
        nums.append(line)

nums.sort()

with open ('output2.txt', 'w') as f:
    f.writelines(nums)


