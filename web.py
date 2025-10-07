from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

BOT_TOKEN = "8255680224:AAH06_qShT8xUjU8BkE1kTnIwhEIF4IQMlE"
WEBHOOK_URL = "https://usmle-helper-bot-x8y3.onrender.com/webhook"  # رابط المشروع على Render + /webhook

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

# Dispatcher لمعالجة الأوامر
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# مثال على أمر /start
def start(update, context):
    update.message.reply_text("أهلا! البوت شغال عن طريق Webhook 🚀")

dispatcher.add_handler(CommandHandler("start", start))

# Route لاستقبال التحديثات من تلغرام
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

# Set webhook تلقائياً عند التشغيل
@app.before_first_request
def setup_webhook():
    bot.delete_webhook()  # يحذف أي webhook قديم
    bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)




    
