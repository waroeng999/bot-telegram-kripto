import os
import requests
from flask import Flask, request

BOT_TOKEN = os.getenv(8287088357)
CHAT_ID = os.getenv(833337630)

app = Flask(__name__)

def send_telegram(msg):
    url = f"https://api.telegram.org/bot8287088357:AAFs0L9F8gkbRTle8sMtYeW5HtrCdQaywfA/sendMessage"
    payload = {
        "chat_id": 833337630,
        "text": msg,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    coin = data.get("coin", "RAJELAS")
    price = data.get("price", "MBUH")
    signal = data.get("signal", "WAIT").upper()
    source = data.get("source", "SENG NGINTIP")
    indicators = data.get("indicators", [])

    emoji = "🟢" if signal == "BUY" else "🔴" if signal == "SELL" else "⚪"

    if signal == "BUY":
        msg = (
            f"{emoji} *JANCUK! WEKTUNE TUKU! 💰🔥*\n"
            f"🚀 Coin: `{coin}`\n"
            f"💵 Rega saiki: *${price}*\n"
            f"📊 Tandha: {', '.join(indicators)}\n"
            f"📡 Sumber: *{source}*\n\n"
            f"📥 Ra kakean cangkem, gekndang tukuo! Selak anyep! 💸🤑"
        )
    elif signal == "SELL":
        msg = (
            f"{emoji} *BAJINDUL! ADOL SEK COK! 🛑🔥*\n"
            f"📉 Coin: `{coin}`\n"
            f"💣 Rega saiki: *${price}*\n"
            f"📊 Tandha jeblug: {', '.join(indicators)}\n"
            f"📡 Sumber: *{source}*\n\n"
            f"⚠️ Ora usah kesuwen, metu wae SU! Sisan nyang kuburan nek nekad! ☠️💀"
        )
    else:
        msg = (
            f"{emoji} *Sabar dab... durung cetha! 😴☕*\n"
            f"🔍 Coin: `{coin}`\n"
            f"💤 Rega saiki: *${price}*\n"
            f"📊 Sing kelihatan: {', '.join(indicators)}\n\n"
            f"📴 Koyo uripmu, ngambang... ngopi disik, ojo sembrono. ☕🧠"
        )

    send_telegram(msg)
    return "ok", 200