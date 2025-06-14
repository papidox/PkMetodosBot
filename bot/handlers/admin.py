
from telegram import Update
from telegram.ext import ContextTypes
import json
import os

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != 'SeuUserAdmin':
        await update.message.reply_text("❌ Acesso negado.")
        return

    afiliados_path = "config/afiliados.json"
    if os.path.exists(afiliados_path):
        with open(afiliados_path) as f:
            afiliados = json.load(f)
        qtd = len(afiliados)
    else:
        qtd = 0

    await update.message.reply_text(
        f"🔧 Painel do Admin:
- Total de afiliados: {qtd}
- Total de códigos disponíveis: verifique config/codigos_promocionais.json"
    )
