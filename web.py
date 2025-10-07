from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

BOT_TOKEN = "8255680224:AAH06_qShT8xUjU8BkE1kTnIwhEIF4IQMlE"
WEBHOOK_URL = "https://usmle-helper-bot-x8y3.onrender.com/webhook"

app = Flask(__name__)

# إنشاء البوت
application = ApplicationBuilder().token(BOT_TOKEN).build()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا! البوت شغال عن طريق Webhook 🚀")

application.add_handler(CommandHandler("start", start))

# Route لاستقبال التحديثات من تلغرام
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return "OK"

# لتعيين webhook عند التشغيل
def setup_webhook():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(application.bot.delete_webhook())
    loop.run_until_complete(application.bot.set_webhook(WEBHOOK_URL))

if __name__ == "__main__":
    setup_webhook()  # هنا بنعين الـ webhook
    app.run(host="0.0.0.0", port=10000)






    
