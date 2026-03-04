from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from notifier import send_notification
from config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running")


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_notification("Test notification")
    await update.message.reply_text("Notification sent")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("System status: OK")


def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))
    app.add_handler(CommandHandler("status", status))

    print("Bot started")

    app.run_polling()


if __name__ == "__main__":
    main()
