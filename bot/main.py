from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from bot.telegram_handlers import start, handle_player_tag, button_handler
from bot.config import TELEGRAM_BOT_TOKEN


def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    
    # Text messages (tags)
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_player_tag)
    )

    # Callback query handler (buttons)
    application.add_handler(CallbackQueryHandler(button_handler))

    print("🚀 Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
