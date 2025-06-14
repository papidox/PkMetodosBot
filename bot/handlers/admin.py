
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def admin_painel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👥 Gerenciar Afiliados", callback_data="admin_afiliados")],
        [InlineKeyboardButton("💰 Chaves Pix", callback_data="admin_pix")],
        [InlineKeyboardButton("📊 Estatísticas", callback_data="admin_stats")],
        [InlineKeyboardButton("🔥 Lançar Promoção", callback_data="admin_promocao")],
        [InlineKeyboardButton("❌ Fechar Painel", callback_data="voltar_menu")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "⚙️ *Painel Administrativo*
Escolha uma opção abaixo:",
        parse_mode='Markdown',
        reply_markup=markup
    )
