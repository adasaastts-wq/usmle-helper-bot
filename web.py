import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
WEBHOOK_URL = "https://usmle-helper-bot-x8y3.onrender.com/webhook"

app = Flask(__name__)
bot_app = ApplicationBuilder().token(BOT_TOKEN).build()

# أمر /start
async def start(update, context):
    await update.message.reply_text("أهلا! البوت شغال 🚀")

bot_app.add_handler(CommandHandler("start", start))

# Route لاستقبال Webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot_app.bot)
    asyncio.create_task(bot_app.process_update(update))
    return "OK"

@app.route("/")
def index():
    return "البوت شغال 🚀"

# إعداد الـ webhook عند الإقلاع
def setup_webhook():
    async def inner():
        await bot_app.bot.delete_webhook()
        await bot_app.bot.set_webhook(WEBHOOK_URL)
        print("✅ Webhook set successfully!")
    asyncio.run(inner())

if __name__ == "__main__":
    setup_webhook()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)














    
