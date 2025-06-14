
from telegram import Update
from telegram.ext import ContextTypes
import os
import random

async def prints(update: Update, context: ContextTypes.DEFAULT_TYPE):
    arquivos = [f for f in os.listdir("prints") if f.endswith(".jpg") or f.endswith(".png")]
    if not arquivos:
        await update.callback_query.message.reply_text("❌ Nenhum print disponível no momento.")
        return
    escolhido = random.choice(arquivos)
    with open(f"prints/{escolhido}", "rb") as img:
        await update.callback_query.message.reply_photo(img, caption="📸 Comprovante de ativação enviado por cliente.")
