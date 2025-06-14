
from telegram import Update
from telegram.ext import ContextTypes

async def metodos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("📁 Você ainda não comprou nenhum método.")
