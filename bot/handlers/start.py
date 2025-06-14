
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.handlers import catalogo, metodos, prints_carrossel, suporte

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📁 Catálogo", callback_data='catalogo')],
        [InlineKeyboardButton("💸 Métodos Ativos", callback_data='metodos')],
        [InlineKeyboardButton("📸 Ativações Recentes", callback_data='prints')],
        [InlineKeyboardButton("👤 Meu Perfil", callback_data='perfil'),
        InlineKeyboardButton("💬 Suporte Técnico", callback_data='suporte')],
        [InlineKeyboardButton("🔔 Últimas Ativações", url='https://t.me/PkMetodosAvisos')]
    ]
    if update.effective_user.id == 6668560082:
        keyboard.append([InlineKeyboardButton("⚙️ Painel Admin", callback_data='admin_painel')])
        [InlineKeyboardButton("📁 Catálogo", callback_data='catalogo')],
        [InlineKeyboardButton("💸 Métodos Ativos", callback_data='metodos')],
        [InlineKeyboardButton("📸 Ativações Recentes", callback_data='prints')],
        [InlineKeyboardButton("👤 Meu Perfil", callback_data='perfil'),
        InlineKeyboardButton("💬 Suporte Técnico", callback_data='suporte')],
        [InlineKeyboardButton("🔔 Últimas Ativações", url='https://t.me/PkMetodosAvisos')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="🔰 Bem-vindo! Escolha uma opção:", reply_markup=markup)

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "catalogo":
        await catalogo.catalogo(update, context)
    elif data == "metodos":
        await metodos.metodos(update, context)
    elif data == "prints":
        await prints_carrossel.prints(update, context)
        await prints.prints(update, context)
    elif data == "suporte":
        await suporte.suporte(update, context)
    else:
        await query.edit_message_text("Função ainda não implementada.")
