import os
import requests as req
from datetime import datetime
from workout import Workout
NUT_ID = "cb9ffb18"
NUT_APP_KEY = os.environ["NUT_APP_KEY"]
GENDER = "male"
WEIGHT = 75
HEIGHT = 178
AGE = 30
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/41635b52676d5df8a9f1efdecffef3cf/workoutTracking/workouts"
SHEETY_AUTH = os.environ["SHEETY_AUTH"]
nut_headers = {
    "x-app-id": NUT_ID,
    "x-app-key": NUT_APP_KEY
}
sheety_headers = {
    "Authorization": SHEETY_AUTH
}


def cal_calories(action_str: str):
    req_body = {
        "query": action_str,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE
    }
    # headers = {
    #     "x-app-id": NUT_ID,
    #     "x-app-key": NUT_APP_KEY
    # }
    return req.post(url=NUT_ENDPOINT, json=req_body, headers=nut_headers)


def save_data_to_googlesheet(data_list):
    lst_res = [req.post(url=SHEETY_ENDPOINT, json=data, headers=sheety_headers).json()
               for data in data_list]
    print(lst_res)


def getdata_from_googlesheet():
    res = req.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
    print(res.json())


def update_data_to_googlesheet(id, req_body):
    res = req.put(url=f"{SHEETY_ENDPOINT}/{id}",
                  json=req_body, headers=sheety_headers).json()
    print(res)
    return res


def delete_data_to_googlesheet(id):
    res = req.delete(url=f"{SHEETY_ENDPOINT}/{str(id)}",
                     headers=sheety_headers)


def main():
    query = input("Tell me what you did today?\n")
    res = cal_calories(query)
    raw_data_list = res.json()["exercises"]
    data_list = [{"workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": x["name"],
        "duration":x["duration_min"],
        "calories":x["nf_calories"],
    }} for x in raw_data_list]
    save_data_to_googlesheet(data_list)
    # getdata_from_googlesheet()
    # update_data_to_googlesheet(8, {"workout": {"duration": 15, "date": "10/12/2021",
    #                            "time": "15:00:00", "exercise": "yoga", "calories": 367.5}})
    # delete_data_to_googlesheet(4)


if __name__ == '__main__':
    main()
