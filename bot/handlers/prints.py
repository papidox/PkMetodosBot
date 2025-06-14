
from telegram import Update
from telegram.ext import ContextTypes
import os
import random

async def prints(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pasta = "prints"
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".jpg") or f.endswith(".png")]
    if not arquivos:
        await update.callback_query.message.reply_text("⚠️ Nenhum print disponível no momento.")
        return
    img = random.choice(arquivos)
    with open(os.path.join(pasta, img), "rb") as f:
        await update.callback_query.message.reply_photo(f, caption="📸 Prova de ativação enviada por cliente.")
