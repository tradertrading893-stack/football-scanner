import asyncio
from scanner import get_today_matches, get_match_info
from telegram_bot import send_message


async def run():
    matches = get_today_matches()

    if not matches:
        await send_message("დღეს შესაბამისი მატჩები ვერ მოიძებნა.")
        return

    text = "⚽ დღევანდელი მატჩები:\n\n"

    for match in matches:
        info = get_match_info(match)

        text += (
            f"🏟 {info['home']} - {info['away']}\n"
            f"ID: {info['id']}\n\n"
        )

    await send_message(text)


if __name__ == "__main__":
    asyncio.run(run())
