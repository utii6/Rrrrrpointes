import os
import threading
from flask import Flask

# 1. إنشاء سيرفر وهمي لإبقاء Koyeb سعيداً
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running and healthy!"

def run_flask():
    # جلب البورت من Koyeb أو استخدام 8000 كافتراضي
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

# 2. تشغيل السيرفر في خلفية منفصلة (Thread)
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# 3. تشغيل ملف البوت الأساسي فوراً
print("--- Starting Telegram Bot ---")
# هذا الأمر سيقوم بتشغيل الملف الذي يحتوي على اتصال Telethon
os.system("python3 ze-telethon-cl.py")
