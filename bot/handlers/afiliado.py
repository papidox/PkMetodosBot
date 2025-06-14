
from telegram import Update
from telegram.ext import ContextTypes
import json

async def afiliado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    with open("config/afiliados.json", "r") as f:
        afiliados = json.load(f)

    if username in afiliados:
        ganhos = afiliados[username].get("ganhos", 0)
        indicados = afiliados[username].get("indicados", 0)
        await update.message.reply_text(
            f"🤝 Painel do Afiliado:
• Indicados: {indicados}
• Ganhos estimados: R${ganhos * 0.5:.2f}
• Link: https://t.me/PkMetodos_Bot?start={username}"
        )
    else:
        await update.message.reply_text("❌ Você ainda não é afiliado.")
