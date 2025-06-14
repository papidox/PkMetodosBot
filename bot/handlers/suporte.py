
from telegram import Update
from telegram.ext import ContextTypes

async def suporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text(
        "🛠️ *Suporte Técnico*

"
        "Caso tenha alguma dúvida, envie sua pergunta diretamente ao nosso suporte humano.

"
        "📩 Telegram: @pkmetodos_suporte
"
        "⏱️ Atendimento: 09h às 22h (todos os dias)",
        parse_mode='Markdown'
    )
