
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.handlers import catalogo, metodos, provas, suporte

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📁 Catálogo", callback_data='catalogo')],
        [InlineKeyboardButton("💸 Métodos Ativos", callback_data='metodos')],
        [InlineKeyboardButton("🧾 Ver Provas", callback_data='provas')],
        [InlineKeyboardButton("💬 Suporte Técnico", callback_data='suporte')],
        [InlineKeyboardButton("🔔 Últimas Ativações", url='https://t.me/PkMetodosAvisos')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="🔰 Bem-vindo! Escolha uma opção:", reply_markup=markup)

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "catalogo":
        await catalogo.catalogo(update, context)
    elif query.data == "metodos":
        await metodos.metodos(update, context)
    elif query.data == "provas":
        await provas.provas(update, context)
    elif query.data == "suporte":
        await suporte.suporte(update, context)
    else:
        await query.edit_message_text(text="Função ainda não implementada.")
