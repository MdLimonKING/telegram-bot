from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8419859681:AAGpjzAREUREatNbbgMiHdfVIMH_gDlcgmg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 হ্যালো!\n\nBot এখন online আছে ✅\nধীরে ধীরে Anime system যোগ করা হবে 🔥"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
