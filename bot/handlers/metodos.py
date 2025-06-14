
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def metodos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📁 Acessar Catálogo", callback_data='catalogo')]]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "📁 Você ainda não comprou nenhum método.
Clique abaixo para acessar o Catálogo.",
        reply_markup=markup
    )
