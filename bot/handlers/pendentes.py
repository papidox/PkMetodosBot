
import json
from telegram import Update
from telegram.ext import ContextTypes

PENDENTES_PATH = "bot/data/compras_pendentes.json"

async def registrar_pendente(user_id, username, metodo):
    with open(PENDENTES_PATH, "r+") as f:
        dados = json.load(f)
        dados.append({"user_id": user_id, "username": username, "metodo": metodo})
        f.seek(0)
        json.dump(dados, f)
        f.truncate()

async def admin_pendentes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(PENDENTES_PATH, "r") as f:
        dados = json.load(f)
    if not dados:
        await update.callback_query.message.reply_text("✅ Nenhuma compra pendente no momento.")
        return
    texto = "🕓 Compras pendentes:

"
    for d in dados:
        texto += f"• @{d['username']} (Método: {d['metodo']})
"
    await update.callback_query.message.reply_text(texto)
