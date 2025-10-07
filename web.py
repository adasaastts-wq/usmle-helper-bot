from flask import Flask, request
import os
from bot import build_app

app = Flask(__name__)
bot_app = build_app()
bot = bot_app.bot

# ====== Home ======
@app.route('/')
def home():
    return "✅ Bot is running!"

# ====== Webhook Endpoint ======
@app.route(f'/{bot.token}', methods=['POST'])
def webhook():
    update = request.get_json(force=True)
    bot_app.update_queue.put(update)
    return "OK"

# ====== Run Flask with Webhook ======
if __name__ == "__main__":
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # رابط البوت النهائي مع التوكن
    bot_app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url_path=f"/{bot.token}",
        webhook_url=WEBHOOK_URL
    )
    
