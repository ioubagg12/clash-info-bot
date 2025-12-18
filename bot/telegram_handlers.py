from telegram import Update
from telegram.ext import ContextTypes
from bot.coc_api import CoCAPI

coc_api = CoCAPI()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    welcome_message = (
        "Clash of Clans Info Bot!       Bunvenit Evreule \n\n"
        "Send me your player tag (e.g. `#P2P2V80C0`) and I will show your stats.\n\n"
        "Commands:\n"
        "/start - Show this message\n"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


async def handle_player_tag(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages that might be player tags"""
    user_input = update.message.text.strip()

    if not user_input:
        await update.message.reply_text(
            "Please send your player tag, for example: `#P2P2V80C0`",
            parse_mode="Markdown",
        )
        return

    await update.message.reply_text(" Fetching player info...", parse_mode="Markdown")

    result = coc_api.get_player_info(user_input)

    if result["success"]:
        data = result["data"]
        name = data.get("name", "Unknown")
        th = data.get("townHallLevel", "N/A")
        trophies = data.get("trophies", "N/A")
        exp = data.get("expLevel", "N/A")
        clan = data.get("clan", {}).get("name", "No clan")

        msg = (
            f"🎮 *{name}*\n\n"
            f"Town Hall: {th}\n"
            f"Trophies: {trophies}\n"
            f"XP Level: {exp}\n"
            f"Clan: {clan}"
        )
        await update.message.reply_text(msg, parse_mode="Markdown")
    else:
        await update.message.reply_text(f"❌ {result['error']}")
