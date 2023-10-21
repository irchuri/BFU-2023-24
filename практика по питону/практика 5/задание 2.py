# set1 = set(map(int, input().split()))
# set2 = set(map(int, input().split()))


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}

if set1 == set2:
    print(False)
else:
    print(set1.issubset(set2))