from flask import Flask
import threading
import bot  # استيراد ملف bot.py

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ USMLE Helper Bot is running on Render!"

# تشغيل البوت في Thread
threading.Thread(target=bot.run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)



    
