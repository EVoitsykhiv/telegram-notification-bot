from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)


def send_notification(message: str):
    bot.send_message(chat_id=CHAT_ID, text=message)
