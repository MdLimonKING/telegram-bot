import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text(
        "👋 হ্যালো!\n\nBot এখন online আছে ✅\nধীরে ধীরে Anime system যোগ করা হবে 🔥"
    )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot started successfully...")
    await app.initialize()
    await app.start()
    await app.bot.initialize()
    await asyncio.Event().wait()  # ⛔ Railway-friendly infinite wait

if __name__ == "__main__":
    asyncio.run(main())
