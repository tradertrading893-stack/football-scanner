import requests


def get_today_matches():
    url = "https://www.sofascore.com/api/v1/sport/football/scheduled-events/2026-07-22"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("events", [])


def get_match_info(event):
    home = event["homeTeam"]["name"]
    away = event["awayTeam"]["name"]

    return {
        "home": home,
        "away": away,
        "id": event["id"]
    }
