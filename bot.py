import asyncio
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

# قراءة التوكن من متغير البيئة
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 USMLE Helper Bot is up and running!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to test if I'm online 😊")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("🚀 Bot started successfully!")
    # 🚫 تعطيل signal handlers لتجنّب الخطأ في thread
    await app.run_polling(stop_signals=None)

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

if __name__ == "__main__":
    run_bot()
