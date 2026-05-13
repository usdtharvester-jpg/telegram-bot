from flask import Flask
from threading import Thread

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ---------------- KEEP ALIVE ---------------- #

app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "BG Wealth Sharing Bot is Running!"

def run():
    app_web.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ---------------- TELEGRAM BOT ---------------- #

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
                url="https://youtube.com/@bgwealthsharinglimitedofficial?si=TE4ZNzByHPNuoity"
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

BOT_TOKEN = "8311716950:AAEqLgTvulrep7a7u5A_7wk2mplSeBIyMt0"

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

keep_alive()

print("Bot is running...")

app.run_polling()
