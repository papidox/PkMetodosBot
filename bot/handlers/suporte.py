
from telegram import Update
from telegram.ext import ContextTypes

async def suporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Suporte disponível:
Fale com @pkmetodos_suporte")
