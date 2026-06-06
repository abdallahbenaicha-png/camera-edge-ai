import requests
import time

# Telegram Bot (optional upgrade)
TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})


def trigger_alert(label):
    msg = f"🚨 ALERT: {label} detected by AI Camera!"
    send_alert(msg)
    print("📡 Alert sent")
