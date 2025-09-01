import requests
import time
import os

FREELANCEHUNT_API = os.getenv("FREELANCEHUNT_API")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def get_projects():
    url = "https://api.freelancehunt.com/v2/projects"
    headers = {"Authorization": f"Bearer {FREELANCEHUNT_API}"}
    r = requests.get(url, headers=headers)
    return r.json().get("data", [])

seen = set()

send_telegram("🤖 Бот запущений і слідкує за новими завданнями!")

while True:
    try:
        projects = get_projects()
        for p in projects:
            pid = p.get("id")
            if pid and pid not in seen:
                seen.add(pid)
                title = p["attributes"]["name"]
                link = p["links"]["self"]
                send_telegram(f"🆕 {title}\n{link}")
    except Exception as e:
        send_telegram(f"⚠️ Помилка: {e}")
    time.sleep(60)
