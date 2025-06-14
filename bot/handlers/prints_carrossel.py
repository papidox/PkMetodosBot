
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import os

user_positions = {}

async def prints(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    arquivos = sorted([f for f in os.listdir("prints") if f.endswith(".jpg") or f.endswith(".png")])
    if not arquivos:
        await update.callback_query.message.reply_text("⚠️ Nenhum print disponível.")
        return

    position = user_positions.get(user_id, 0)
    if position >= len(arquivos):
        position = 0

    nome_arquivo = arquivos[position]
    legenda = f"📸 Prova de ativação {position + 1} de {len(arquivos)}"
    keyboard = []
    if len(arquivos) > 1:
        keyboard = [[
            InlineKeyboardButton("⬅ Anterior", callback_data='print_anterior'),
            InlineKeyboardButton("➡ Próximo", callback_data='print_proximo')
        ]]
    markup = InlineKeyboardMarkup(keyboard)

    with open(f"prints/{nome_arquivo}", "rb") as img:
        await update.callback_query.message.reply_photo(img, caption=legenda, reply_markup=markup)

    user_positions[user_id] = position

async def prints_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    arquivos = sorted([f for f in os.listdir("prints") if f.endswith(".jpg") or f.endswith(".png")])
    if not arquivos:
        await query.edit_message_text("⚠️ Nenhum print disponível.")
        return

    position = user_positions.get(user_id, 0)
    if query.data == "print_proximo":
        position = (position + 1) % len(arquivos)
    elif query.data == "print_anterior":
        position = (position - 1) % len(arquivos)

    nome_arquivo = arquivos[position]
    legenda = f"📸 Prova de ativação {position + 1} de {len(arquivos)}"
    keyboard = [[
        InlineKeyboardButton("⬅ Anterior", callback_data='print_anterior'),
        InlineKeyboardButton("➡ Próximo", callback_data='print_proximo')
    ]]
    markup = InlineKeyboardMarkup(keyboard)

    with open(f"prints/{nome_arquivo}", "rb") as img:
        await query.edit_message_reply_photo(photo=img, caption=legenda, reply_markup=markup)

    user_positions[user_id] = position
