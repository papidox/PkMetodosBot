
import os
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from bot.handlers import start

token = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start.start))
app.add_handler(CallbackQueryHandler(start.menu_callback))

print("Bot rodando...")
app.run_polling()
