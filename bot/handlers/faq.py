
from telegram import Update
from telegram.ext import ContextTypes

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 *FAQ - Perguntas Frequentes*\n\n"
        "1️⃣ Como recebo o método?\n"
        "▶️ Após o pagamento, o método é liberado automaticamente.\n\n"
        "2️⃣ O que é o código na descrição?\n"
        "▶️ É o código gerado para identificar seu pagamento.\n\n"
        "3️⃣ Em quanto tempo recebo?\n"
        "▶️ Liberação automática em até 10 minutos.\n\n"
        "4️⃣ Tem suporte?\n"
        "▶️ Sim, fale com @pkmetodos_suporte"
    , parse_mode='Markdown')
