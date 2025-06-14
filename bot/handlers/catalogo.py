
from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.payment import chave_pix_ativa, gerar_codigo_pagamento

async def catalogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.username or update.effective_user.first_name
    chave_pix = chave_pix_ativa()
    codigo = gerar_codigo_pagamento(user)
    msg = '🛍️ *Catálogo de Métodos Disponíveis*\n\n'
    msg += '• Nubank Pagamento Fantasma – R$100\n  Guia atualizado para gerar faturas reversíveis.\n\n'
    msg += '• iFood Cashback 2025 – R$90\n  Técnica para ativar cashback oculto em contas antigas.\n\n'
    msg += f'\n💰 *Pagamento:*\nChave Pix: `{chave_pix}`\nCódigo: `{codigo}`\n'
    msg += 'Envie o comprovante aqui mesmo após o pagamento. Liberação em até 10 minutos.'
    await update.callback_query.message.reply_text(msg, parse_mode='Markdown')
