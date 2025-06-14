
import json
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

PROMOCAO_PATH = "bot/data/promocoes.json"

async def admin_promocao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("✍️ Envie o percentual da promoção (ex: 20 para 20%):")
    context.user_data["admin_action"] = "definir_promocao"

async def tratar_resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    action = context.user_data.get("admin_action")
    if action == "definir_promocao":
        try:
            percentual = int(update.message.text.strip())
            fim = datetime.now() + timedelta(hours=24)
            dados = {
                "ativa": True,
                "porcentagem": percentual,
                "fim": fim.strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(PROMOCAO_PATH, "w") as f:
                json.dump(dados, f)
            await update.message.reply_text(f"🔥 Promoção de {percentual}% ativada por 24h!
Notificando usuários...")
            # Simular envio a todos (em sistema real, você leria todos os users registrados)
        except:
            await update.message.reply_text("❌ Valor inválido. Tente novamente.")
    context.user_data["admin_action"] = None
