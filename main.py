
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from bot.handlers import start, catalogo, metodos, prints_carrossel, suporte, perfil, admin, afiliados, pix, promocao, pendentes
from config.config import BOT_TOKEN

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Comando /start
    application.add_handler(CommandHandler("start", start.start))
    application.add_handler(CallbackQueryHandler(start.menu_callback, pattern="^voltar_menu$"))

    # Botões principais
    application.add_handler(CallbackQueryHandler(catalogo.catalogo, pattern="^catalogo$"))
    application.add_handler(CallbackQueryHandler(metodos.metodos, pattern="^metodos$"))
    application.add_handler(CallbackQueryHandler(prints_carrossel.prints_menu, pattern="^prints$"))
    application.add_handler(CallbackQueryHandler(suporte.suporte, pattern="^suporte$"))
    application.add_handler(CallbackQueryHandler(perfil.perfil, pattern="^perfil$"))

    # Painel Admin
    application.add_handler(CallbackQueryHandler(admin.painel_admin, pattern="^admin_painel$"))
    application.add_handler(CallbackQueryHandler(afiliados.admin_afiliados, pattern="^afiliados_admin$"))
    application.add_handler(CallbackQueryHandler(pix.admin_pix, pattern="^pix_admin$"))
    application.add_handler(CallbackQueryHandler(promocao.admin_promocao, pattern="^promo_admin$"))
    application.add_handler(CallbackQueryHandler(pendentes.admin_pendentes, pattern="^pendentes_admin$"))

    # Ações administrativas (mensagem após botão)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, afiliados.tratar_resposta))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, pix.tratar_resposta))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, promocao.tratar_resposta))

    application.run_polling()

if __name__ == "__main__":
    main()
