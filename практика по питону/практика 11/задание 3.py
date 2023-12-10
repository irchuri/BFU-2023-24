import csv
from collections import defaultdict
import matplotlib.pyplot as plotlib


with open('passengers.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [(row['Month'], int(row['#Passengers'])) for row in reader]

years = sorted(set(month[:4] for month, _ in data))
data_months = defaultdict(list)
for month, passenger in data:
    data_months[month[5:]].append(passenger)


plotlib.figure(figsize=(12, 6))
plotlib.plot(years, [sum(passenger for month, passenger in data if month.startswith(year)) for year in years])
plotlib.title('Пассажиропоток за все время')
plotlib.xlabel('Года')
plotlib.ylabel('Количество пассажиров')
plotlib.xticks(rotation=45)
plotlib.tight_layout()
plotlib.show()


plotlib.figure(figsize=(12, 6))
for month, values in data_months.items():
    plotlib.bar(month, sum(values), label=month, color = 'pink')


plotlib.title('Распределение пассажиров по месяцам (1951-1955)')
plotlib.xlabel('Месяцы')
plotlib.ylabel('Количество пассажиров')
plotlib.show()