
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

AFILIADOS_PATH = "bot/data/afiliados.json"

async def admin_afiliados(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(AFILIADOS_PATH, "r") as f:
        afiliados = json.load(f)

    texto = "👥 *Afiliados Atuais:*
" + "\n".join([f"- @{a}" for a in afiliados]) if afiliados else "Nenhum afiliado registrado."
    teclado = [
        [InlineKeyboardButton("➕ Adicionar", callback_data="afiliado_add"),
         InlineKeyboardButton("➖ Remover", callback_data="afiliado_remover")],
        [InlineKeyboardButton("🔙 Voltar", callback_data="admin_menu")]
    ]
    markup = InlineKeyboardMarkup(teclado)
    await update.callback_query.message.reply_text(texto, parse_mode='Markdown', reply_markup=markup)

async def add_afiliado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("✍️ Envie o username do novo afiliado (sem @):")
    context.user_data["admin_action"] = "add_afiliado"

async def remover_afiliado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("❌ Envie o username do afiliado a remover (sem @):")
    context.user_data["admin_action"] = "remover_afiliado"

async def tratar_resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    action = context.user_data.get("admin_action")
    user = update.message.text.strip().replace("@", "")
    if action == "add_afiliado":
        with open(AFILIADOS_PATH, "r+") as f:
            dados = json.load(f)
            if user not in dados:
                dados.append(user)
                f.seek(0)
                json.dump(dados, f)
                f.truncate()
        await update.message.reply_text(f"✅ @{user} adicionado como afiliado.")
    elif action == "remover_afiliado":
        with open(AFILIADOS_PATH, "r+") as f:
            dados = json.load(f)
            if user in dados:
                dados.remove(user)
                f.seek(0)
                json.dump(dados, f)
                f.truncate()
        await update.message.reply_text(f"🗑️ @{user} removido da lista de afiliados.")
    context.user_data["admin_action"] = None
