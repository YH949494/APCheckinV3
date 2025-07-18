from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TELEGRAM_TOKEN = '7620072160:AAEbty9W7vqZ5sgNAY8I0ACWYCIiNVrNZDs'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message and message.text:
        if not message.text.lower().startswith("#checkin"):
            try:
                await message.delete()
            except Exception as e:
                print(f"Failed to delete message: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
