import requests
import time
import json
import telebot

TELEGRAM_BOT_TOKEN = "توکن_ربات_تو_اینجا_بزار"
CHAT_ID = "ایدی_چت_تلگرام_تو_اینجا_بزار"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def check_pump():
    url = "https://api.dexscreener.com/latest/dex/tokens"
    response = requests.get(url)
    data = response.json()

    for token in data['pairs']:
        price_change = float(token['priceChange']['h24'])
        volume = float(token['volume']['h24'])
        symbol = token['baseToken']['symbol']
        dex = token['dexId']

        if price_change > 15:
            message = f"🚀 پامپ شناسایی شد! \n🔹 ارز: {symbol} \n📈 تغییر قیمت: {price_change}% \n📊 حجم معاملات: {volume} \n🏦 صرافی: {dex}"
            send_telegram_message(message)

while True:
    check_pump()
    time.sleep(300)  # هر ۵ دقیقه اجرا شود
