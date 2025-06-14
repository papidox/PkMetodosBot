
from telegram import Update
from telegram.ext import ContextTypes
import os
import random

async def prints(update: Update, context: ContextTypes.DEFAULT_TYPE):
    arquivos = [f for f in os.listdir("prints") if f.endswith(".jpg") or f.endswith(".png")]
    if not arquivos:
        await update.message.reply_text("📷 Nenhum print disponível no momento.")
        return
    escolha = random.choice(arquivos)
    with open(f"prints/{escolha}", "rb") as f:
        await update.message.reply_photo(f, caption="📸 Prova de pagamento enviada por cliente.")
