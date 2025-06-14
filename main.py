
import os
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from bot.handlers import start

token = os.getenv("7565675198:AAFTGLzXZa88KRxBmjob4fMDuP2tUrt6Dvg")
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start.start))
app.add_handler(CallbackQueryHandler(start.menu_callback))

print("Bot está rodando...")
app.run_polling()
