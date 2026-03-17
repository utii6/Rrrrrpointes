import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_server():
    # المنصة ستعطي البورت تلقائياً عبر متغير PORT
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

# تشغيل السيرفر في خلفية البوت
Thread(target=run_server).start()

# الآن يبدأ كود البوت الأصلي الخاص بك بالأسفل...

import threading
import os

def run_script(script_name):
    os.system(f'python3 {script_name}')

scripts = []

threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

