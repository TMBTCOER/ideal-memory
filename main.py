import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import google.generativeai as genai

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your Grocery Assistant Bot. How can I help you today?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can ask me about grocery items, recipes, or place an order.")

# Define message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = model.generate_content(user_message)
        await update.message.reply_text(response.text)
    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("Sorry, I encountered an error while processing your request.")

# Main function to run the bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
