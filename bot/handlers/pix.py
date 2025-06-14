
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

PIX_PATH = "bot/data/pix.json"

async def admin_pix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(PIX_PATH, "r") as f:
        chaves = json.load(f)

    texto = "💰 *Chaves Pix Atuais:*
" + "\n".join([f"- {c}" for c in chaves])
    teclado = [
        [InlineKeyboardButton("➕ Adicionar", callback_data="pix_add"),
         InlineKeyboardButton("➖ Remover", callback_data="pix_remover")],
        [InlineKeyboardButton("🔙 Voltar", callback_data="admin_menu")]
    ]
    markup = InlineKeyboardMarkup(teclado)
    await update.callback_query.message.reply_text(texto, parse_mode='Markdown', reply_markup=markup)

async def add_pix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("✍️ Envie a nova chave Pix:")
    context.user_data["admin_action"] = "add_pix"

async def remover_pix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text("❌ Envie a chave Pix a remover:")
    context.user_data["admin_action"] = "remover_pix"

async def tratar_resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    action = context.user_data.get("admin_action")
    chave = update.message.text.strip()
    if action == "add_pix":
        with open(PIX_PATH, "r+") as f:
            dados = json.load(f)
            if chave not in dados:
                dados.append(chave)
                f.seek(0)
                json.dump(dados, f)
                f.truncate()
        await update.message.reply_text(f"✅ Chave Pix adicionada.")
    elif action == "remover_pix":
        with open(PIX_PATH, "r+") as f:
            dados = json.load(f)
            if chave in dados:
                dados.remove(chave)
                f.seek(0)
                json.dump(dados, f)
                f.truncate()
        await update.message.reply_text(f"🗑️ Chave Pix removida.")
    context.user_data["admin_action"] = None
