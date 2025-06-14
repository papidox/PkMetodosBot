
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def perfil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("🔙 Voltar ao Menu", callback_data='voltar_menu')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        f"👤 *Seu Perfil*\n\n"
        f"• Nome: {user.full_name}\n"
        f"• Username: @{user.username if user.username else 'Não definido'}\n"
        f"• ID: {user.id}\n\n"
        "Você poderá acompanhar aqui suas compras, saldo de afiliado e outros recursos futuros.",
        parse_mode='Markdown',
        reply_markup=markup
    )