from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.coc_api import CoCAPI

coc_api = CoCAPI()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    welcome_message = (
        "Clash of Clans Info Bot!       Bunvenit Evreule \n\n"
        "Send me a tag (e.g. `#P2P2V80C0`) and choose if it's a Player or Clan.\n\n"
        "Commands:\n"
        "/start - Show this message\n"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


async def handle_player_tag(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages that might be tags"""
    user_input = update.message.text.strip()

    if not user_input:
        await update.message.reply_text(
            "Please send a tag, for example: `#P2P2V80C0`",
            parse_mode="Markdown",
        )
        return

    # Store the tag in user_data to use it in the callback
    context.user_data["tag"] = user_input

    keyboard = [
        [
            InlineKeyboardButton("Player Info", callback_data="player"),
            InlineKeyboardButton("Clan Info", callback_data="clan"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Is this a Player tag or a Clan tag?", reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button clicks"""
    query = update.callback_query
    await query.answer()

    choice = query.data
    tag = context.user_data.get("tag")

    if not tag:
        await query.edit_message_text(text="Session expired. Please send the tag again.")
        return

    if choice == "player":
        await query.edit_message_text(text="Fetching player info...")
        result = coc_api.get_player_info(tag)
        
        if result["success"]:
            data = result["data"]
            name = data.get("name", "Unknown")
            th = data.get("townHallLevel", "N/A")
            trophies = data.get("trophies", "N/A")
            exp = data.get("expLevel", "N/A")
            clan = data.get("clan", {}).get("name", "No clan")
            builderth = data.get("builderHallLevel", "N/A")
            warstars = data.get("warStars", "N/A") 
            besttrophies = data.get("bestTrophies", "N/A")
            buildertrophies = data.get("builderBaseTrophies", "N/A")

            msg = (
                f"🎮 *{name}*\n\n"
                f"Town Hall: {th}\n"
                f"Trophies: {trophies}\n"
                f"XP Level: {exp}\n"
                f"Clan: {clan}\n"
                f"War Stars: {warstars}\n"
                f"Best Trophies: {besttrophies}\n"
                f"Builder Hall: {builderth}\n"  
                f"Builder Base Trophies: {buildertrophies}\n"
            )
            await query.message.reply_text(msg, parse_mode="Markdown")
        else:
            await query.message.reply_text(f" {result['error']}")

    elif choice == "clan":
        await query.edit_message_text(text="Fetching clan info...")
        result = coc_api.get_clan_info(tag)

        if result["success"]:
            data = result["data"]
            name = data.get("name", "Unknown")
            level = data.get("clanLevel", "N/A")
            members = data.get("members", "N/A")
            points = data.get("clanPoints", "N/A")
            description = data.get("description", "No description")
            
            msg = (
                f"🛡️ *{name}*\n\n"
                f"Level: {level}\n"
                f"Members: {members}\n"
                f"Points: {points}\n"
                f"Description: {description}\n"
            )
            await query.message.reply_text(msg, parse_mode="Markdown")
        else:
            await query.message.reply_text(f" {result['error']}")
