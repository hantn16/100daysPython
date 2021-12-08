import json
import requests as req
from datetime import datetime
X_TOKEN = "dfdkfjdkflsjdlkfjdkfjdkfdfdkk"
USER_NAME = "hantn16"


def create_graph():
    graph_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
    graph_info = {
        "id": "g1",
        "name": "Coding Time",
        "unit": "hour",
        "type": "float",
        "color": "sora"
    }
    headers = {
        "X-USER-TOKEN": X_TOKEN,
    }
    return req.post(url=graph_endpoint, json=graph_info, headers=headers)


def create_user():
    pixela_endpoint = "https://pixe.la/v1/users"
    user_info = {
        "token": X_TOKEN,
        "username": USER_NAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    return req.post(url=pixela_endpoint, json=user_info)


def post_pixel(graph_id: str, day_str: str, value: float):
    endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{graph_id}"
    headers = {
        "X-USER-TOKEN": X_TOKEN,
    }
    req_body = {
        "date": day_str,
        "quantity": str(value),
    }
    return req.post(url=endpoint, json=req_body, headers=headers)


def update_pixel(graph_id: str, day_str: str, value: float):
    endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{graph_id}/{day_str}"
    print(day_str)
    print(endpoint)
    headers = {
        "X-USER-TOKEN": X_TOKEN,
    }
    req_body = {
        "quantity": str(value),
    }
    return req.put(url=endpoint, json=req_body, headers=headers)


def delete_pixel(graph_id: str, day_str: str):
    endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{graph_id}/{day_str}"
    print(day_str)
    print(endpoint)
    headers = {
        "X-USER-TOKEN": X_TOKEN,
    }
    return req.delete(url=endpoint, headers=headers)


def main():

    # create_graph_res = create_graph()
    # post_pixel_res = post_pixel(
    #     graph_id="g1", day_str=datetime(year=2021, month=12, day=7).strftime("%Y%m%d"), value=4.0)
    # update_pixel_res = update_pixel(
    #     graph_id="g1", day_str=datetime(year=2021, month=12, day=7).strftime("%Y%m%d"), value=2.0)
    delete_pixel_res = delete_pixel(
        graph_id="g1", day_str=datetime(year=2021, month=12, day=7).strftime("%Y%m%d"))
    print(delete_pixel_res.text)


if __name__ == '__main__':
    main()
