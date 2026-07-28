import os
import requests

# خواندن اطلاعات از متغیرهای محیطی گیت‌هاب اکشن
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHANNEL_USERNAME = os.environ.get("CHANNEL_ID")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def generate_ai_news():
    """تولید متن خبر با استفاده از هوش مصنوعی OpenAI"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "تو یک نویسنده حرفه‌ای اخبار فناوری و هوش مصنوعی هستی. یک خلاصه کوتاه، جذاب و جذاب به زبان فارسی درباره آخرین پیشرفت‌های هوش مصنوعی بنویس."
            },
            {
                "role": "user",
                "content": "لطفا یک گزارش کوتاه و جذاب درباره جدیدترین اتفاقات دنیای هوش مصنوعی بنویس."
            }
        ],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            print(f"خطا در ارتباط با OpenAI: {response.text}")
            return "🤖 *گزارش روزانه هوش مصنوعی*\n\nامروز سیستم با خطا در دریافت متن از هوش مصنوعی مواجه شد."
    except Exception as e:
        print(f"خطا: {e}")
        return "🤖 *گزارش روزانه هوش مصنوعی*\n\nخطا در تولید محتوا."

def send_telegram_message(message):
    """ارسال پیام به کانال تلگرام"""
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
    print("در حال تولید اخبار با هوش مصنوعی...")
    news_text = generate_ai_news()
    
    print("در حال ارسال به کانال تلگرام...")
    send_telegram_message(news_text)
