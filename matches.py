import requests
from datetime import datetime


BASE_URL = "https://www.sofascore.com/api/v1"


def get_today_matches():

    today = datetime.now().strftime("%Y-%m-%d")

    url = f"{BASE_URL}/sport/football/scheduled-events/{today}"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("events", [])
