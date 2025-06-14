
from telegram import Update
from telegram.ext import ContextTypes

async def afiliado_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.username
    if not user:
        await update.message.reply_text("❌ É necessário ter um username para gerar link.")
        return

    link = f"https://t.me/PkMetodos_Bot?start={user}"
    await update.message.reply_text(f"🔗 Seu link de afiliado:
{link}")
