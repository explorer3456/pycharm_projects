import csv
import pandas
from numpy.ma.extras import average

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

    # print(temperature)

# how to read CSV file using panda
data = pandas.read_csv("weather_data.csv")

# Panda data frame data. Data frame means whole data
print(type(data))
print(data)

# Panda data serires data. Data serires means certain row of data
print(type(data["temp"]))
print(data["temp"])

# convert data serires into data list.
temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = average(temp_list)
print(avg_temp)

# Panda data series object support mean,max meathod.
print(data["temp"].mean())
print(data["temp"].max())

# Panda data series object add row name attribute automatically.
# data["temp"] is same as data.temp.
print(data.temp)

