import os
import asyncio
import nest_asyncio
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# ---------------------- إعدادات البوت ----------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
WEBHOOK_URL = "https://usmle-helper-bot-x8y3.onrender.com/webhook"

nest_asyncio.apply()
app = Flask(__name__)
bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
initialized = False

# ---------------------- أوامر البوت ----------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎯 **Welcome to USMLE_sources!**\n\n"
        "Your all-in-one USMLE study companion 🩺\n\n"
        "Use /help to see available commands 🚀"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 Commands:\n"
        "/start - Intro\n"
        "/help - This help\n"
        "/anki - Get Anki decks\n"
        "/uworld - UWorld strategies\n"
        "/books - High-yield books\n"
        "/beyond - Boards & Beyond\n"
        "/schedule - Study schedule\n"
        "/about - About bot"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 USMLE_sources — Your all-in-one USMLE study companion! 🚀")

# ---------------------- /anki command ----------------------
async def anki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🧠 BNB", callback_data="anki_bnb"),
            InlineKeyboardButton("🧠 CNS", callback_data="anki_cns")
        ],
        [
            InlineKeyboardButton("💪 MSK", callback_data="anki_msk"),
            InlineKeyboardButton("👶 Reproductive", callback_data="anki_reproductive")
        ],
        [
            InlineKeyboardButton("🩸 Hematology & Oncology", callback_data="anki_hem_onc"),
            InlineKeyboardButton("📚 Step1 Deck", callback_data="anki_step1")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📚 Choose a deck to download:", reply_markup=reply_markup)

async def anki_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    decks = {
        "anki_bnb": "🧠 *BNB Deck*\n🔗 [Download here](https://example.com/bnb)",
        "anki_cns": "🧠 *CNS Deck*\n🔗 [Download here](https://example.com/cns)",
        "anki_msk": "💪 *MSK Deck*\n🔗 [Download here](https://example.com/msk)",
        "anki_reproductive": "👶 *Reproductive Deck*\n🔗 [Download here](https://example.com/reproductive)",
        "anki_hem_onc": "🩸 *Hematology & Oncology Deck*\n🔗 [Download here](https://example.com/hem_onc)",
        "anki_step1": "📚 *Step1 Deck*\n🔗 [Download here](https://example.com/step1)"
    }

    response = decks.get(query.data, "⚠️ Deck not found.")
    await query.edit_message_text(text=response, parse_mode="Markdown")

# ---------------------- رد تلقائي للرسائل ----------------------
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "hi" in text or "hello" in text or "مرحبا" in text:
        await update.message.reply_text("👋 Hey there! Type /help to see what I can do.")
    else:
        await update.message.reply_text("🤖 Type /help to explore USMLE_sources commands!")

# ---------------------- إضافة الهاندلرز ----------------------
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("help", help_cmd))
bot_app.add_handler(CommandHandler("about", about))
bot_app.add_handler(CommandHandler("anki", anki))
bot_app.add_handler(CallbackQueryHandler(anki_buttons))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))

# ---------------------- Flask routes ----------------------
@app.route("/")
def home():
    return "✅ USMLE_sources Bot is Live!"

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

    loop = asyncio.get_event_loop()
    loop.create_task(process())
    return "OK", 200

# ---------------------- إعداد الـ webhook ----------------------
async def setup_webhook():
    await bot_app.bot.delete_webhook()
    await bot_app.bot.set_webhook(WEBHOOK_URL)
    print("✅ Webhook set successfully!")

loop = asyncio.get_event_loop()
loop.run_until_complete(setup_webhook())




