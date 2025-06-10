
from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler

TOKEN = "TON_TOKEN_ICI"  # Remplace par ton vrai token

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def start_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    def start(update, context):
        update.message.reply_text("Bot bien lancé ! 😎")

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

Thread(target=start_bot).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
