from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8255680224:AAH06_qShT8xUjU8BkE1kTnIwhEIF4IQMlE"
WEBHOOK_URL = "https://usmle-helper-bot-x8y3.onrender.com/webhook"  # رابط المشروع على Render + /webhook

app = Flask(__name__)

# إنشاء البوت عن طريق ApplicationBuilder
application = ApplicationBuilder().token(BOT_TOKEN).build()

# مثال على أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا! البوت شغال عن طريق Webhook 🚀")

application.add_handler(CommandHandler("start", start))

# Route لاستقبال التحديثات من تلغرام
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return "OK"

# Set webhook تلقائياً عند التشغيل
@app.before_first_request
def setup_webhook():
    application.bot.delete_webhook()
    application.bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)





    
