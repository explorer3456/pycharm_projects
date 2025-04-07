import csv

# legacy file opeartion for CSV
with open("weather_data.csv") as file:
    data = file.readlines()
    data_strip = []
    for d in data:
        d.strip('\n')
        data_strip.append(d)

# we can use library CSV to read CSV format file more easily
with open("weather_data.csv") as file:
    data_csv = csv.reader(file)
    temperature = []
    for row in data_csv:
        if row[1] != "temp":
            temperature.append(int(row[1]))

print(temperature)



