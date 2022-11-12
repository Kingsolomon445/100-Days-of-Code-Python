# reading csv data

import csv

import pandas as pd

with open("weather_data.csv") as data:
    data = csv.reader(data)

new_data = pd.read_csv("weather_data.csv")

temp_file = new_data["temp"]  # or new_data.temp
temp_lst = temp_file.to_list()


monday = new_data[new_data.day == "Monday"]
monday_temp = monday.temp
print(monday_temp)

# converting the celcius temp to fahrenheit
new_monday_temp = monday_temp * 1.8 + 32
print(new_monday_temp)
