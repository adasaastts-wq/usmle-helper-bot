import os
import asyncio
import nest_asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
WEBHOOK_URL = "https://usmle-helper-bot-x8y3.onrender.com/webhook"
PORT = int(os.environ.get("PORT", 10000))

nest_asyncio.apply()  # 🔥 مهم جدًا لتجنب مشاكل loop داخل Flask

app = Flask(__name__)
bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
initialized = False

# أوامر البوت
async def start(update, context):
    await update.message.reply_text("🚀 البوت شغال تمام!")

async def help_cmd(update, context):
    await update.message.reply_text("استخدم /start لتتأكد إنو البوت شغال ✅")

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("help", help_cmd))

@app.route("/")
def home():
    return "✅ USMLE Helper Bot is Live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    global initialized
    data = request.get_json(force=True)
    update = Update.de_json(data, bot_app.bot)

    async def process():
        global initialized
        if not initialized:
            await bot_app.initialize()
            initialized = True
        await bot_app.process_update(update)

    # استخدم create_task بدل asyncio.run
    loop = asyncio.get_event_loop()
    loop.create_task(process())

    return "OK", 200

def main():
    print("☁️ Running on Render (Webhook mode)")
    async def setup():
        await bot_app.bot.delete_webhook()
        await bot_app.bot.set_webhook(WEBHOOK_URL)
        print("✅ Webhook set successfully!")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup())

    app.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    main()

