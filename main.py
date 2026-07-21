import asyncio

from scanner import get_today_matches, get_match_info
from telegram_bot import send_message
from filters import match_passes_filter


async def run():

    matches = get_today_matches()

    found = []

    for match in matches:

        info = get_match_info(match)

        # აქ შემდეგ ეტაპზე ჩაერთვება
        # ბოლო 2 თამაშის სტატისტიკის შემოწმება

        team_a_stats = {
            "shots": 0,
            "shots_on_target": 0,
            "corners": 0
        }

        team_b_stats = {
            "shots": 0,
            "shots_on_target": 0,
            "corners": 0
        }

        if match_passes_filter(team_a_stats, team_b_stats):

            found.append(
                f"⚽ {info['home']} - {info['away']}"
            )


    if found:
        message = "🔥 ნაპოვნი თამაშები:\n\n"
        message += "\n".join(found)

    else:
        message = "დღეს შესაბამისი თამაში ვერ მოიძებნა."


    await send_message(message)


if __name__ == "__main__":
    asyncio.run(run())
