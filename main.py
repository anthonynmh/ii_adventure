import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import load_dotenv

load_dotenv()


TOKEN: Final = os.getenv('TOKEN')
BOT_USERNAME: Final = os.getenv('BOT_USERNAME')


# Commands
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("Hello! I am iiAdventureBot - I can help in your travel planning.")


# Responses
def handle_response(text: str) -> str:
  processed_text: str = text.lower()

  return processed_text
  
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type
  text: str = update.message.text.strip()

  if message_type == "group":
    if BOT_USERNAME in text:
      text: str = text.replace(BOT_USERNAME, '')
    
  res = handle_response(text)
  await update.message.reply_text(res)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
  app = Application.builder().token(TOKEN).build()

  # commands
  app.add_handler(CommandHandler('start', start_cmd))

  # messages
  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  # errors
  app.add_error_handler(error)

  # polling rate
  app.run_polling(poll_interval=3)