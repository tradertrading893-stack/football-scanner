import requests


BASE_URL = "https://www.sofascore.com/api/v1"


def get_team_last_matches(team_id):
    url = f"{BASE_URL}/team/{team_id}/events/last/0"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("events", [])[:2]


def get_match_statistics(match_id):
    url = f"{BASE_URL}/event/{match_id}/statistics"

    response = requests.get(url)

    if response.status_code != 200:
        return {}

    return response.json()
