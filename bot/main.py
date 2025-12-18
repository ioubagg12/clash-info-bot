from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.telegram_handlers import start,  handle_player_tag
from bot.config import TELEGRAM_BOT_TOKEN


def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("help", help_command))
    # Text messages (player tags)
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_player_tag)
    )

    print("🚀 Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
