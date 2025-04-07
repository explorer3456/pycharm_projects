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

# How to access row data using Panda ?
# ex) find row that has maximum temperature.
print(data[data.temp == data.temp.max()])

# how to access single column data using Panda ?
monday_data = data[data.day == "Monday"]
print(monday_data)
print(monday_data.temp) # 0 12 (i.e 0 is index, 12 is actual temperature )
print(monday_data.temp[0]) # 12 (i.e 12 is actual temperature )

# Create data frame from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 67, 33]
}

# Covert data frame into csv files
my_data_frame = pandas.DataFrame(data_dict)
print(my_data_frame)
print(my_data_frame.to_csv("./my_new_csv.csv"))

