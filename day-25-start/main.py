# with open("./weather_data.csv", "r") as f:
#     data = f.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# s: int = 0
# for temp in temp_list:
#     s += int(temp)
# print(s / len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
# print(data["condition"])
# print(data.condition)

# get data in rows
# print(data[data.day == "Monday"])

# get the row with the highest temperature
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print((monday.temp*1.8) + 32)

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [34, 22, 56]
# }
# data_from_scratch = pandas.DataFrame(data_dict)
# print(data_from_scratch)
# data_from_scratch.to_csv("new_data.csv")

data = pandas.read_csv("central_park_squirrel.csv")
black_dict = data[data["Primary Fur Color"] == "Black"].to_dict()
black_number = len(black_dict["Primary Fur Color"])

# black_squirrels_count = data[data["Primary Fur Color"] == "Black"]
# black_number = len(black_squirrels_count)

grey_dict = data[data["Primary Fur Color"] == "Gray"].to_dict()
grey_number = len(grey_dict["Primary Fur Color"])

red_dict = data[data["Primary Fur Color"] == "Cinnamon"].to_dict()
red_number = len(red_dict["Primary Fur Color"])

count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_number, red_number, black_number]
}

count_dict_from_scratch = pandas.DataFrame(count_dict)
count_dict_from_scratch.to_csv("squirrel_count.csv")
