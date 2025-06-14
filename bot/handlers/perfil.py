
from telegram import Update
from telegram.ext import ContextTypes

async def perfil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.callback_query.message.reply_text(
        f"👤 *Seu Perfil*

"
        f"🆔 ID: `{user.id}`
"
        f"📛 Nome: {user.first_name}
"
        f"📬 Username: @{user.username if user.username else 'N/A'}

"
        "📦 Histórico de compras: em breve disponível.",
        parse_mode='Markdown'
    )
