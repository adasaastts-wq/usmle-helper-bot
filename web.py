from flask import Flask
import threading
import asyncio
import os
from bot import main  # async main()

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running successfully on Render!"

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
