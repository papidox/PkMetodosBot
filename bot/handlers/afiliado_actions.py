
from telegram import Update
from telegram.ext import ContextTypes

async def afiliado_actions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Ações do Afiliado:
"
        "- Ver total de vendas
"
        "- Solicitar saque (fake)
"
        "- Alterar nome do link"
    )
