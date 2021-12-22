import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os


# API_KEY = "70e70b7bba20c47997ff50e5e0659ff4"
# APP_ID = "6f3c7c5d"
API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# USERNAME = "akwoo39"
# PASSWORD = "reenielovesgorgor"
# TOKEN = "Bearer gorgorlovesreenie"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
TOKEN = os.environ["TOKEN"]

project_name = "myWorkout"
file_name = "workouts"

Query = input("Write down exercises you have done")
header = {
    "x-app-id":"6f3c7c5d",
    "x-app-key":"70e70b7bba20c47997ff50e5e0659ff4"
}
workout_params = {
    "query":Query,
    "gender":"female",
    "weight_kg":69,
    "height_cm":163,
    "age":29

}

workout_response = requests.post(url=exercise_endpoint,json=workout_params,headers=header)
workout_data = workout_response.json()
exercise_data = workout_data["exercises"]

sheety_endpoint = "https://api.sheety.co/8b6c843d0b5584ab3894f9aee99bd4ce/myWorkouts/workouts"
bearer_token = {"Authorization": TOKEN}


for exercise in range(len(exercise_data)):
    timestamp = datetime.now()
    date = timestamp.strftime("%d/%m/%Y")
    time = timestamp.strftime("%H:%M:%S")
    duration = exercise_data[exercise]["duration_min"]
    calories = exercise_data[exercise]["nf_calories"]
    exercise = exercise_data[exercise]["name"].title()
    # print(exercise_data[exercise])
    sheety_params = {
        "workout":
            {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
    }
    # bearer authentication
    # sheety_response = requests.post(url=sheety_endpoint,json=sheety_params,headers=bearer_token)
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, auth=(USERNAME,PASSWORD))

    print(sheety_response.text)

