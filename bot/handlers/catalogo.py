
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def catalogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Bancos", callback_data="cat_bancos")],
        [InlineKeyboardButton("🍔 Alimentação", callback_data="cat_alimentacao")],
        [InlineKeyboardButton("🛍 Lojas Online", callback_data="cat_lojas")],
        [InlineKeyboardButton("🚗 Multas e IPVA", callback_data="cat_ipva")],
        [InlineKeyboardButton("💸 Premiums", callback_data="cat_premium")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text("📦 Escolha uma categoria de métodos:", reply_markup=markup)
