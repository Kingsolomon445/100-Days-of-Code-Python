# The great squirrel census data analysis

import pandas as pd

# This gets the primary fur colors and the total count of each and represent the data in a new csv file

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_list = fur_color.to_list()
colors = list(set(fur_color_list))
counts = [fur_color_list.count(color) for color in colors]
data_dict = {
    "fur color": colors,
    "count": counts
}
new_data = pd.DataFrame.from_dict(data_dict)
new_data.to_csv("squirrel_count")



