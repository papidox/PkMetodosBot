
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def suporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👨‍💻 Falar com o Suporte", url="https://t.me/pkmetodos_suporte")],
        [InlineKeyboardButton("🔙 Voltar ao Menu", callback_data='voltar_menu')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "🛠️ *Suporte Técnico*\n\n"
        "Caso esteja com dúvidas, pagamentos em aberto ou precise de ajuda com os métodos, clique no botão abaixo e fale com nosso time.\n\n"
        "Estamos online todos os dias para te ajudar.",
        parse_mode='Markdown',
        reply_markup=markup
    )