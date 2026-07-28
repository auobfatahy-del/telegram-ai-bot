import os
import requests
from google import genai

# خواندن متغیرهای محیطی
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHANNEL_USERNAME = os.environ.get("CHANNEL_ID")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def generate_ai_news():
    """تولید متن خبر با استفاده از هوش مصنوعی جمنای"""
    try:
        # مقداردهی اولیه کلاینت جمنای
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        prompt = "یک گزارش کوتاه، جذاب و حرفه‌ای به زبان فارسی درباره آخرین پیشرفت‌ها و اخبار دنیای هوش مصنوعی بنویس."
        
        # استفاده از مدل استاندارد و فعال
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
        )
        
        return response.text
    except Exception as e:
        print(f"خطا در ارتباط با جمنای: {e}")
        return "🤖 *گزارش روزانه هوش مصنوعی*\n\nامروز سیستم با خطا در دریافت متن از جمنای مواجه شد."

def send_telegram_message(message):
    """ارسال پیام به کانال تلگرام"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
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
    print("در حال تولید اخبار با جمنای...")
    news_text = generate_ai_news()
    
    print("در حال ارسال به کانال تلگرام...")
    send_telegram_message(news_text)
