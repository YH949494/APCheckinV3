from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import os
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if not update.message.text.strip().lower().startswith("#checkin"):
            try:
                await update.message.delete()
                logging.info(f"Deleted: {update.message.text}")
            except Exception as e:
                logging.warning(f"Could not delete: {e}")
        else:
            logging.info(f"Allowed: {update.message.text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
logging.info("Bot is running...")
app.run_polling()
