import os
import requests


def send_message(text):

    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.post(url, data=data)

    print("STATUS:", response.status_code)
    print("ANSWER:", response.text)
