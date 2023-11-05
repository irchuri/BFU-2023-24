import json
import csv

with open('Sample-employee-JSON-data.json') as f:
    data = json.loads(f.read())
print(data)
data1 = data["Employees"]
print(data1)
dict_keys = list(data1[0].keys())
print(dict_keys)

v = csv.writer("test.csv", "wb+")
v.writerow(dict_keys)
