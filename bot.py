import os
import asyncio
import nest_asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

# 🧩 اجلب التوكن من متغير البيئة BOT_TOKEN
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# 🧠 الأوامر الأساسية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 USMLE Helper Bot is up and running!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to test if I'm online 😊")

# 🚀 الدالة الرئيسية لتشغيل البوت
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("🚀 Bot started successfully and running polling...")
    await app.run_polling(stop_signals=None)

# 🔄 استدعاء البوت داخل Flask
def run_bot():
    nest_asyncio.apply()
    asyncio.run(main())

