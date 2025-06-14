
from telegram import Update
from telegram.ext import ContextTypes

async def metodos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📁 Você ainda não comprou nenhum método. Realize o pagamento para liberar o conteúdo.")
