from flask import Flask
import threading
import asyncio
import os
from bot import main  # async def main()

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running successfully on Render!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # شغّل Flask في Thread منفصل
    threading.Thread(target=run_flask).start()

    # شغّل البوت باستخدام asyncio بدون إعادة تشغيل loop
    loop = asyncio.get_event_loop()
    loop.create_task(main())  # شغّل البوت بدون blocking
    loop.run_forever()        # خلّي الـ loop شغّالة
    
