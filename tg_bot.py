from flask import Flask
from threading import Thread

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------------- WEB SERVER ---------------- #

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is alive!"

def run_web():
    web.run(host="0.0.0.0", port=10000)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# ---------------- TELEGRAM BOT ---------------- #

TOKEN = "8311716950:AAE2IJiRk1dQZzEDaUwOe1oJPLTMgNR1TFI"

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

# ---------------- MAIN ---------------- #

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

keep_alive()

print("Bot started successfully!")

app.run_polling(drop_pending_updates=True)
