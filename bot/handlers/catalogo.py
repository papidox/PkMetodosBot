
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def catalogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏦 Bancos", callback_data='categoria_bancos')],
        [InlineKeyboardButton("🛒 Compras Online", callback_data='categoria_compras')],
        [InlineKeyboardButton("🚗 Multas e IPVA", callback_data='categoria_multas')],
        [InlineKeyboardButton("📱 Apps Digitais", callback_data='categoria_apps')],
        [InlineKeyboardButton("🔙 Voltar ao Menu", callback_data='voltar_menu')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "🛒 *Catálogo de Métodos Atuais*\n\n"
        "Nossos métodos são atualizados semanalmente e passam por verificação manual.\n"
        "Escolha abaixo a categoria que mais se encaixa no que você procura:",
        parse_mode='Markdown',
        reply_markup=markup
    )