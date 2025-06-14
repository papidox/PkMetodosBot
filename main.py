
# main.py
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.handlers.start import start

app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()
app.add_handler(CommandHandler("start", start))

print("Bot rodando...")
app.run_polling()
