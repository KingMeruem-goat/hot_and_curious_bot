
from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler

TOKEN = "7771606520:AAFp9ZonHi-MSgi1Jah_M9KmrgGKzH9v_Lk"  

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
# Fausse ligne pour Render pour qu'il détecte un port et démarre bien le service
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

if name == "__main__":
    import asyncio
    from bot import main  # Remplace ça par ta fonction principale si elle a un autre nom
    loop = asyncio.get_event_loop()
    loop.create_task(main())  # Lance ton bot
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
