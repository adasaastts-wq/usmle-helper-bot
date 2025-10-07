from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا 👋! أنا بوت مساعد USMLE.")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("الأوامر المتاحة:\n/anki\n/uworld\n/books\n/bnb")

async def anki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧩 روابط ونصائح أنكي")

async def uworld(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 استراتيجيات UWorld")

async def books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 كتب عالية الفائدة")

async def bnb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎥 Boards & Beyond")

# الدالة الرئيسية بصيغة async
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("anki", anki))
    app.add_handler(CommandHandler("uworld", uworld))
    app.add_handler(CommandHandler("books", books))
    app.add_handler(CommandHandler("bnb", bnb))

    print("✅ Bot is running... Ctrl+C to stop")
    await app.run_polling()
