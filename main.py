from scanner import check_match
from telegram_bot import send_message
from matches import get_today_matches
async def run():

    matches = get_today_matches()

    results = []

    for match in matches:
        ...
