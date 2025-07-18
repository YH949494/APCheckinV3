import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Set your token here directly OR use environment variable
TOKEN = os.getenv("TELEGRAM_TOKEN") or "YOUR_TELEGRAM_BOT_TOKEN"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    text = update.message.text.strip()

    if not text.lower().startswith("#checkin"):
        try:
            await update.message.delete()
        except Exception as e:
            print(f"Failed to delete message: {e}")
    else:
        try:
            await update.message.delete()
            # You can add XP logic here
        except Exception as e:
            print(f"Failed to delete check-in message: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running with long polling...")
    app.run_polling()
