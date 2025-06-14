
from telegram import Update
from telegram.ext import ContextTypes

async def provas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📂 Acesse o canal @PkMetodosAvisos para ver as ativações recentes.")
