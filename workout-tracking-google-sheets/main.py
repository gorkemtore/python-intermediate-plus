import os
from datetime import datetime
import requests as requests

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 174
AGE = 21


APP_ID = os.environ.get("GOOGLE_SHEETS_APP_ID")
API_KEY = os.environ.get("GOOGLE_SHEETS_APP_KEY")
GOOGLE_SHEETS_TOKEN = os.environ.get("GOOGLE_SHEETS_TOKEN")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/13f5b674da81e864a813bea26ccf8355/workoutTracking/workouts"


exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
     "query": exercise_text,
     "gender": GENDER,
     "weight_kg": WEIGHT_KG,
     "height_cm": HEIGHT_CM,
     "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()["exercises"]

print(result)

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": GOOGLE_SHEETS_TOKEN
}
for exercise in result:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
