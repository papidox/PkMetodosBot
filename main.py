
# main.py
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.handlers.start import start

app = ApplicationBuilder().token("7565675198:AAFTGLzXZa88KRxBmjob4fMDuP2tUrt6Dvg").build()
app.add_handler(CommandHandler("start", start))

print("Bot rodando...")
app.run_polling()
