from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8255680224:AAH06_qShT8xUjU8BkE1kTnIwhEIF4IQMlE"
WEBHOOK_URL = "https://usmle-helper-bot-x8y3.onrender.com/webhook"

app = Flask(__name__)
bot_app = ApplicationBuilder().token(BOT_TOKEN).build()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا! البوت شغال 🚀")

bot_app.add_handler(CommandHandler("start", start))

# Route لاستقبال Webhook
@app.route("/webhook", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    await bot_app.update_queue.put(update)
    return "OK"

@app.route("/")
def index():
    return "البوت شغال 🚀"

# حذف وتعيين Webhook عند التشغيل
async def setup_webhook():
    await bot_app.bot.delete_webhook()
    await bot_app.bot.set_webhook(WEBHOOK_URL)
    # بدء البوت لمعالجة الرسائل
    await bot_app.start()
    await bot_app.updater.start_polling()  # هذا آمن حتى مع Webhook

if __name__ == "__main__":
    import asyncio
    asyncio.run(setup_webhook())
    app.run(host="0.0.0.0", port=10000)









    
