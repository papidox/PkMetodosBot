
from telegram import Update
from telegram.ext import ContextTypes

async def suporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("📞 Suporte disponível:\nFale com @pkmetodos_suporte")
