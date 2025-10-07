from flask import Flask
import threading
import os
from bot import main  # استدعاء دالة main من ملف البوت

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running successfully on Render!"

def run_bot():
    main()

if __name__ == "__main__":
    # شغّل البوت في خيط منفصل
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
