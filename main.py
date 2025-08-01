import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes 

# Replace this with your own token from BotFather
TOKEN = "8453661836:AAFijylDj1AA9RslUQcN_bpdsjCJXiFCtPo" 

logging.basicConfig(level=logging.INFO) 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your downloader bot.") 

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start)) 

app.run_polling()