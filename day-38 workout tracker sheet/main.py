import requests
from datetime import datetime

GENDER = YOUR_GENDER
WEIGHT_KG = YOUR_WEIGHT
HEIGHT_CM = YOUR_HEIGHT
AGE = YOUR_AGE
BEARER_TOKEN = "YOUR BEARER TOKEN"

APP_ID = YOUR_APP_ID
APP_KEY = YOUR_APP_KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "YOUR_SHEET_ENDPOINT"

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_input = input("Tell me about which exercises you did: ")

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE 
}

response = requests.post(exercise_endpoint, json=parameters, headers=header)
result = response.json()

################## Create a new Row in the google Sheet #################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": BEARER_TOKEN
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)