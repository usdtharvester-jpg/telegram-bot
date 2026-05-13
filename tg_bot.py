from flask import Flask
from threading import Thread
import asyncio

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------------- FLASK ---------------- #

web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "BG Bot Running Successfully!"

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# ---------------- TELEGRAM BOT ---------------- #

BOT_TOKEN = "8311716950:AAE2IJiRk1dQZzEDaUwOe1oJPLTMgNR1TFI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📢 Join Telegram",
                url="https://t.me/bgwealthsharinglimited"
            )
        ],
        [
            InlineKeyboardButton(
                "▶️ YouTube Channel",
                url="https://youtube.com/@bgwealthsharinglimitedofficial"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🚀 Welcome to BG Wealth Sharing Limited Bot!\n\n"
        "👉 Join our community & watch latest updates:",
        reply_markup=reply_markup
    )

async def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started successfully!")

    await app.run_polling()

# ---------------- START ---------------- #

keep_alive()

asyncio.run(main())
