import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(data["temp"].to_list())/len(data["temp"])
print(average)

mean_method_avg = data["temp"].mean()
print(mean_method_avg)

print(data["temp"].max())

#Get Data in column
print(data.condition)

#Get Data in row
print(data[data.day == "Monday"])

#Challenge, tempeture is at maximum
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp
print(int(monday_temp)*9/5+32)
monday_temp_F = int(monday_temp)*9/5 + 32
print(f"Monday Fahrenheit temp is {monday_temp_F}")

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


sq_data = pandas.read_csv("squirrel_count.csv")
grey_sq = sq_data[sq_data["Primary Fur Color"] == "Gray"]

red_sq = sq_data[sq_data["Primary Fur Color"] == "Cinnamon"]
black_sq = sq_data[sq_data["Primary Fur Color"] == "Black"]
grey_sq_num = len(grey_sq)
black_sq_num = len(black_sq)
red_sq_num = len(red_sq)

sq_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Number": [grey_sq_num, red_sq_num, black_sq_num]
}
sq_data = pandas.DataFrame(sq_dict)
sq_data = sq_data.to_csv("sq_data.csv")