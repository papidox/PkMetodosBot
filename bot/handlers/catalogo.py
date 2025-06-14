
from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.payment import chave_pix_ativa, gerar_codigo_pagamento

async def catalogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.username or update.effective_user.first_name
    chave_pix = chave_pix_ativa()
    codigo = gerar_codigo_pagamento(user)

    msg = '🎯 *Catálogo de Métodos Disponíveis*\n\n'
    msg += '💳 *Bancos*\n• Nubank Pagamento Fantasma – R$100\n  Guia para gerar faturas reversíveis.\n\n'
    msg += '🍔 *Alimentação*\n• iFood Cashback 2025 – R$90\n  Técnica para ativar cashback oculto.\n\n'
    msg += '🛍 *Lojas Online*\n• Americanas Cupom Gold – R$75\n  Método para ativar cupons expirados.\n\n'
    msg += '🚗 *Multas e IPVA*\n• Desbloqueio IPVA 2025 – R$150\n  Técnica de isenção via protocolo.\n\n'
    msg += '💸 *Métodos Premium*\n• Método Amazon Elite – R$250\n  Acesso a bugs de giftcard ocultos.\n\n'
    msg += f'💰 *Pagamento:*\nChave Pix: `{chave_pix}`\nCódigo: `{codigo}`\n'
    msg += 'Envie o comprovante aqui mesmo após o pagamento. Liberação automática.'
    await update.callback_query.message.reply_text(msg, parse_mode='Markdown')
