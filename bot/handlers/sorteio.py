
from telegram import Update
from telegram.ext import ContextTypes
import json
import random

async def sorteio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("config/inscritos_sorteio.json", "r") as f:
        inscritos = json.load(f)

    if len(inscritos) < 100:
        await update.message.reply_text("🎁 Ainda não há 100 inscritos. Continue indicando!")
        return

    ganhador = random.choice(inscritos)
    codigo = f"SORTE{random.randint(1000,9999)}"

    with open("config/codigos_promocionais.json", "r+") as f:
        codigos = json.load(f)
        codigos.append({"codigo": codigo, "usado": False})
        f.seek(0)
        json.dump(codigos, f, indent=2)

    await update.message.reply_text(f"🎉 Novo ganhador: @{ganhador}
Código gerado: {codigo}")
