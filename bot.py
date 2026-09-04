import requests
import time

TOKEN = "توکن_بات_خودت"

API = f"https://tapi.bale.ai/bot{TOKEN}"

GAME_URL = "https://doniadideamirhosein-alt.github.io/my_game/"

def send_message(chat_id, text):
    url = f"{API}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "🎮 شروع بازی",
                        "web_app": {
                            "url": GAME_URL
                        }
                    }
                ]
            ]
        }
    }

    requests.post(url, json=data)


offset = 0

while True:
    try:
        result = requests.get(
            f"{API}/getUpdates",
            params={"offset": offset, "timeout": 30}
        ).json()

        for update in result.get("result", []):
            offset = update["update_id"] + 1

            message = update.get("message", {})
            text = message.get("text", "")
            chat_id = message.get("chat", {}).get("id")

            if text == "/start" and chat_id:
                send_message(
                    chat_id,
                    "🎮 به بازی خوش آمدید!\n\nبرای شروع روی دکمه زیر بزنید:"
                )

    except Exception as e:
        print("Error:", e)

    time.sleep(1)
