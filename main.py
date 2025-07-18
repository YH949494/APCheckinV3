import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from flask import Flask, request

TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = f"https://telegram-checkin-bot-v3.fly.dev/{TOKEN}"

app = Flask(__name__)

telegram_app = ApplicationBuilder().token(TOKEN).build()

# Only allow #checkin, delete others
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.strip()
        await update.message.delete()

telegram_app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    telegram_app.update_queue.put(Update.de_json(request.get_json(force=True), telegram_app.bot))
    return "ok"

@app.route("/")
def home():
    return "Bot is running!"

# Set webhook on startup
if __name__ == "__main__":
    import asyncio
    asyncio.run(telegram_app.bot.set_webhook(WEBHOOK_URL))
    app.run(host="0.0.0.0", port=8080)
