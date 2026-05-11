from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📢 Join Telegram", url="https://t.me/bgwealthsharinglimited")],
        [InlineKeyboardButton("▶️ YouTube Channel", url="https://youtube.com/@bgwealthsharinglimitedofficial?si=TE4ZNzByHPNuoity")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🚀 Welcome to BG Bot!\n\n"
        "👉 Join our community & watch updates:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token("8311716950:AAGgO3h3GoGgKhNNTeAYF3TWtWQPA0uT7oM").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()