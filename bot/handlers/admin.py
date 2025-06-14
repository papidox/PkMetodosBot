
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def painel_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧑‍💼 Afiliados", callback_data="afiliados_admin")],
        [InlineKeyboardButton("💳 Chaves Pix", callback_data="pix_admin")],
        [InlineKeyboardButton("🎯 Promoções", callback_data="promo_admin")],
        [InlineKeyboardButton("⏳ Pendentes", callback_data="pendentes_admin")],
        [InlineKeyboardButton("🔙 Voltar ao Menu", callback_data="voltar_menu")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "⚙️ *Painel Administrativo*\n\n"
        "Use as opções abaixo para gerenciar afiliados, chaves Pix, promoções e usuários pendentes.\n\n"
        "Essa área é exclusiva para administradores.",
        parse_mode='Markdown',
        reply_markup=markup
    )