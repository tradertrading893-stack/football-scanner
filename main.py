from telegram_bot import send_message
from matches import get_today_matches


async def run():

    send_message("✅ ტესტი: Football Scanner ბოტი მუშაობს")

    matches = get_today_matches()

    print("დღევანდელი თამაშების რაოდენობა:", len(matches))


if __name__ == "__main__":
    import asyncio
    asyncio.run(run())
