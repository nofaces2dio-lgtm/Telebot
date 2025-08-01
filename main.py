import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes 

# Replace this with your own token from BotFather
TOKEN = 8224767817:AAE1l_Kyf5tY7K_FNjJkneI0nTFbMbnSDNs" 

logging.basicConfig(level=logging.INFO) 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your downloader bot.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start)) 

app.run_polling()