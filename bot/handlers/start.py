from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.handlers import catalogo, metodos, prints_carrossel, suporte, perfil, admin

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📁 Catálogo", callback_data='catalogo')],
        [InlineKeyboardButton("💸 Métodos Ativos", callback_data='metodos')],
        [InlineKeyboardButton("📸 Ativações Recentes", callback_data='prints')],
        [InlineKeyboardButton("👤 Meu Perfil", callback_data='perfil'), InlineKeyboardButton("💬 Suporte Técnico", callback_data='suporte')],
        [InlineKeyboardButton("🔔 Últimas Ativações", url='https://t.me/PkMetodosAvisos')]
    ]

    if update.effective_user.id == 6668560082:
        keyboard.append([InlineKeyboardButton("⚙️ Painel Admin", callback_data='admin_painel')])

    markup = InlineKeyboardMarkup(keyboard)
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id,
        text="🔰 *Bem-vindo ao Pk Métodos!*\n\n"
             "Aqui você encontra os melhores métodos, bugs e informações para garantir sua renda extra diária. 💸\n\n"
             "Atualizamos nossos conteúdos constantemente com o que há de mais recente e eficaz. Alguns métodos podem envolver riscos e não seguem todas as normas legais -- portanto, o uso é 100% sob sua responsabilidade. ⚠️\n\n"
             "Aproveite com consciência. Nossa equipe está aqui para te ajudar no que precisar!",
        parse_mode='Markdown',
        reply_markup=markup
    )

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "catalogo":
        await catalogo.catalogo(update, context)
    elif data == "metodos":
        await metodos.metodos(update, context)
    elif data == "prints":
        await prints_carrossel.prints_menu(update, context)
    elif data == "suporte":
        await suporte.suporte(update, context)
    elif data == "perfil":
        await perfil.perfil(update, context)
    elif data == "admin_painel":
        await admin.painel_admin(update, context)
    elif data == "voltar_menu":
        await start(update, context)