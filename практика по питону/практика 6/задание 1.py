with open ('file1.txt') as f:
    line = f.readline()

nums = list(map(int, line.split()))
prod = 1
for num in nums:
    prod *= num

with open('output1.txt', 'w') as f:
    f.write(str(prod))