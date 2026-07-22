import os
import requests


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


async def send_message(text):

    if not BOT_TOKEN or not CHAT_ID:
        print("BOT_TOKEN ან CHAT_ID არ მოიძებნა")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }



print("Telegram პასუხი:")
print(response.text)
         
                            
                            
                            
                
    







          
