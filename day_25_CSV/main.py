import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"].max())
# print(data.temp.max())
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data.temp.to_list()
# print(temp_list)

# print(data.temp.mean())
# print(data[data.temp > 21])
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"])
monday = data[data.day == "Monday"]
print(monday)
# monday_temp = int(monday.temp)
print(int(monday.temp))
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour": ["gray", "red", "black"],
    "Count": [gray_count, red_count, black_count]
    }

data_csv = pandas.DataFrame(data_dict)

data_csv.to_csv("data_csv.csv")
