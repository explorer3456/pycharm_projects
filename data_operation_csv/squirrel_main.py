import pandas

sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_sq = sq_data[sq_data["Primary Fur Color"] == "Gray"]
red_sq = sq_data[sq_data["Primary Fur Color"] == "Cinnamon"]
black_sq = sq_data[sq_data["Primary Fur Color"] == "Black"]

print(len(grey_sq))
print(len(red_sq))
print(len(black_sq))

data_dict = {
    "Fur" : ['Grey', 'Red', 'Black'],
    "Count" : [len(grey_sq), len(red_sq), len(black_sq)]
}

print(data_dict)

my_data = pandas.DataFrame(data_dict)

print(my_data)