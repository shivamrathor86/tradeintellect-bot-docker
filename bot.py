from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Welcome to TradeIntellectAI – India’s Trading Mentor Bot\n"
        "📈 Get Signals | 🎓 Learn Trading | 🧠 Ask Anything"
    )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
