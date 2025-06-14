
from telegram import Update
from telegram.ext import ContextTypes
import os
import random

async def prints(update: Update, context: ContextTypes.DEFAULT_TYPE):
    arquivos = os.listdir("prints")
    if not arquivos:
        await update.callback_query.message.reply_text("⚠️ Nenhum print disponível.")
        return
    escolhido = random.choice(arquivos)
    with open(f"prints/{escolhido}", "rb") as img:
        await update.callback_query.message.reply_photo(img, caption="📸 Comprovante real de cliente.")
