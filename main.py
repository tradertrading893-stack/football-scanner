import asyncio

from scanner import check_match
from telegram_bot import send_message


# აქ დროებით მოგვაქვს მატჩები
# შემდეგ ეტაპზე დავუკავშირებთ Sofascore-ის დღევანდელ მატჩებს

matches = []


async def run():

    results = []

    for match in matches:

        data = check_match(match)

        if data:

            results.append(
                f"⚽ {data['home']} - {data['away']}\n"
                f"🏠 გუნდი A: {data['home_stats']}\n"
                f"🚩 გუნდი B: {data['away_stats']}\n"
            )


    if results:

        message = (
            "🔥 ნაპოვნი მატჩები:\n\n"
            + "\n".join(results)
        )

    else:

        message = (
            "დღეს შენი კრიტერიუმებით "
            "მატჩი ვერ მოიძებნა."
        )


    await send_message(message)


if __name__ == "__main__":
    asyncio.run(run())
