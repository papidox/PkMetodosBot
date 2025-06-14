
from telegram import Update
from telegram.ext import ContextTypes

async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 Área VIP desbloqueada apenas para membros especiais.
"
        "Métodos exclusivos de valor elevado.

"
        "Acesse o suporte e solicite acesso: @pkmetodos_suporte"
    )
