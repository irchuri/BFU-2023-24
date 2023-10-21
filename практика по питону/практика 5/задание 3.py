n = int(input())
cities = set()
for i in range(n):
    cities.add(input())
len_old = len(cities)
cities.add(input())
len_new = len(cities)
if len_old == len_new:
    print("REPEAT")
else:
    print("OK")