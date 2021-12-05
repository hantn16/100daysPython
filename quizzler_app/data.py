import requests
params = {
    "amount": 10,
    "type": "boolean"
}
res = requests.get("https://opentdb.com/api.php", params)
res.raise_for_status()
question_data = res.json()["results"]
