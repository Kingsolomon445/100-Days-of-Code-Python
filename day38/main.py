import requests
import os
from datetime import datetime

# -----------------------------Getting a json file for workout query----------------------------------#
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
HEIGHT, WEIGHT, AGE = 183.0, 80.0, 23
EXERCISE_HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
query = input("What workout did you do today?: ")
ex_params = {
    "query": query,
    "gender": "male",
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
exercise_endP = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=exercise_endP, json=ex_params, headers=EXERCISE_HEADER)
response.raise_for_status()
result = response.json()

# -----------------------------Updating the google sheet datas------------------#
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")
exercise_list = []
for exercise in result["exercises"]:
    pair = {}
    for key, value in exercise.items():
        if key == "name":
            pair["exercise"] = value.title()
        elif key == "duration_min":
            pair["duration"] = round(value)
        elif key == "nf_calories":
            pair["calories"] = round(value)
    pair["date"] = date
    pair["time"] = time
    exercise_list.append(pair)

sheety_endP = "https://api.sheety.co/2e5a24157faf35a913235ea8279cbde8/myWorkouts/workouts"
for exercise in exercise_list:
    sheety_params = {"workout": {key: value for key, value in exercise.items()}}
    response = requests.post(url=sheety_endP,
                             json=sheety_params,
                             auth=(os.environ.get("SHEETY_USERNAME"),
                                   os.environ.get("SHEETY_PASSWORD")),
                             )
    response.raise_for_status()
    print(response.text)
