import os
import requests

# خواندن توکن و آیدی کانال از متغیرهای محیطی گیت‌هاب اکشن
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHANNEL_USERNAME = os.environ.get("CHANNEL_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("پیام با موفقیت به کانال ارسال شد!")
    else:
        print(f"خطا در ارسال پیام: {response.text}")

if __name__ == "__main__":
    # متن خبری که ربات می‌خواهد ارسال کند
    news_text = "🤖 *گزارش روزانه هوش مصنوعی*\n\nامروز خبرهای مهمی در دنیای هوش مصنوعی منتشر شده است که به زودی بررسی می‌شوند..."
    
    send_telegram_message(news_text)
