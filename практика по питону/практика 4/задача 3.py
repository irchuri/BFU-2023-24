#arr = list(input().split())

arr = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
counts = []

t = []
for i in arr:
    if i not in t:
        t.append(i)

for i in range(0, len(t)):
    counts.append(arr.count(t[i]))

print(*counts)