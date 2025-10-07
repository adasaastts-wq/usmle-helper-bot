import os
import asyncio
import nest_asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

# --- إعداد التوكن ---
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# --- تعريف الأوامر ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 USMLE Helper Bot is up and running on Render!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to check if I'm online 😊")

# --- الدالة الرئيسية لتشغيل البوت ---
async def main():
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN not found in environment variables!")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🚀 Bot started successfully!")
    await app.run_polling(stop_signals=None)

# --- وظيفة الاستدعاء من web.py ---
def run_bot():
    nest_asyncio.apply()
    asyncio.run(main())

    

