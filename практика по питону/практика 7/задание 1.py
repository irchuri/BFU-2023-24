import json
import csv

with open('Sample-employee-JSON-data.json') as f:
    json_data = json.load(f)

data = json_data[(list(dict.items(json_data))[0])[0]]

with open("output.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    count = 0
    for item in data:
        if count == 0:
            header = item.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(item.values())