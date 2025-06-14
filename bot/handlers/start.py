
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📁 Catálogo", callback_data='catalogo')],
        [InlineKeyboardButton("💸 Métodos Ativos", callback_data='metodos')],
        [InlineKeyboardButton("🧾 Ver Provas", callback_data='provas')],
        [InlineKeyboardButton("💬 Suporte Técnico", callback_data='suporte')],
        [InlineKeyboardButton("🔔 Últimas Ativações", url='https://t.me/PkMetodosAvisos')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔰 Bem-vindo! Escolha uma opção:", reply_markup=markup)

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Você clicou: {query.data}")
