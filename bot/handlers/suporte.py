
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def suporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔙 Voltar ao Menu", callback_data='voltar_menu')]]
    markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "🛠️ *Suporte Técnico*

"
        "Tem alguma dúvida, problema com pagamento ou precisa de ajuda com um método?

"
        "Fale diretamente com nosso suporte humano:
"
        "📩 @pkmetodos_suporte

"
        "⏱️ *Atendimento*: Todos os dias das 09h às 22h

"
        "🔐 Respeite o prazo de resposta e evite mensagens repetidas.",
        parse_mode='Markdown',
        reply_markup=markup
    )
