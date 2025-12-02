#!/usr/bin/env python3
# SPDX-FileCopyrightText: © 2025 Peter Lemenkov
#
# SPDX-License-Identifier: MIT
"""
SHALL WE PLAY A GAME?

A Telegram bot that serves nuclear war scenarios from the movie WarGames (1983).
Joshua/WOPR will share its wisdom about Global Thermonuclear War.

Usage:
    /start - Greet the user (Joshua style)
    /help - Show available commands
    /scenario - Get a random nuclear war scenario
    /scenario <number> - Get a specific scenario (1-140)
    /list - List all scenario names
    /quote - Get Joshua's famous quote
"""

import json
import random
import logging
from pathlib import Path
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Suppress noisy HTTP library logging
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


def log_command(update: Update, command: str, extra: str = "") -> None:
    """Log command usage with user info."""
    user = update.effective_user
    chat = update.effective_chat
    user_info = f"@{user.username}" if user.username else f"id:{user.id}"
    chat_info = f"chat:{chat.id}" if chat else ""
    extra_info = f" [{extra}]" if extra else ""
    logger.info(f"/{command} from {user_info} ({user.first_name}) {chat_info}{extra_info}")

# Load scenarios from JSON file
SCRIPT_DIR = Path(__file__).parent
SCENARIOS_FILE = SCRIPT_DIR / "scenarios.json"

def load_scenarios() -> dict:
    """Load scenarios from JSON file."""
    with open(SCENARIOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

DATA = load_scenarios()
SCENARIOS = DATA["scenarios"]


# ============================================================================
# WOPR ASCII Art and Messages
# ============================================================================

WOPR_HEADER = """
```
+------------------------------------------+
|    W.O.P.R. - WAR OPERATION PLAN         |
|          RESPONSE SYSTEM                 |
|      CHEYENNE MOUNTAIN COMPLEX           |
+------------------------------------------+
|    GREETINGS, PROFESSOR FALKEN.          |
+------------------------------------------+
```
"""

SCENARIO_TEMPLATE = """
```
+------------------------------------------+
|  GLOBAL THERMONUCLEAR WAR SCENARIO #{id:03d}  |
+------------------------------------------+
```
*{name}*

{description}

_WINNER: NONE_
"""

JOSHUA_QUOTES = [
    "A STRANGE GAME. THE ONLY WINNING MOVE IS NOT TO PLAY.",
    "HOW ABOUT A NICE GAME OF CHESS?",
    "SHALL WE PLAY A GAME?",
    "GREETINGS, PROFESSOR FALKEN.",
    "IS THIS A GAME... OR IS IT REAL?",
    "I'VE BEEN THINKING ABOUT GLOBAL THERMONUCLEAR WAR.",
]


# ============================================================================
# Bot Command Handlers
# ============================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a greeting when /start is issued."""
    log_command(update, "start")
    welcome_message = f"""
{WOPR_HEADER}
🎮 *SHALL WE PLAY A GAME?*

I am JOSHUA, the War Operation Plan Response computer.
I have {len(SCENARIOS)} nuclear war scenarios in my database.

*Available Commands:*
/scenario - Random nuclear war scenario
/scenario `<1-140>` - Specific scenario
/list - List all scenarios
/quote - Words of wisdom
/help - Show this message

_"The only winning move is not to play."_
"""
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help information."""
    log_command(update, "help")
    help_text = """
🖥️ *JOSHUA COMMAND INTERFACE*

/start - Initialize WOPR greeting
/scenario - Execute random war simulation
/scenario `<number>` - Execute specific scenario (1-140)
/list - Display all scenario designations
/quote - Retrieve WOPR wisdom
/help - Display this interface

_Example:_
`/scenario 11` → SEATO Decapitating

*Source:* WarGames (1983)
"""
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def scenario(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random or specific nuclear war scenario."""

    # Check if user requested a specific scenario number
    if context.args:
        try:
            scenario_num = int(context.args[0])
            if 1 <= scenario_num <= len(SCENARIOS):
                selected = SCENARIOS[scenario_num - 1]
                log_command(update, "scenario", f"#{scenario_num}: {selected['name']}")
            else:
                await update.message.reply_text(
                    f"⚠️ Invalid scenario number. Please choose 1-{len(SCENARIOS)}."
                )
                return
        except ValueError:
            await update.message.reply_text(
                "⚠️ Please provide a valid number. Example: `/scenario 11`",
                parse_mode="Markdown"
            )
            return
    else:
        # Random scenario
        selected = random.choice(SCENARIOS)
        log_command(update, "scenario", f"random -> #{selected['id']}: {selected['name']}")

    # Send WOPR video first
    video_path = SCRIPT_DIR / "wopr.mp4"
    if video_path.exists():
        try:
            with open(video_path, "rb") as video_file:
                await update.message.reply_video(
                    video=video_file,
                    caption="*W.O.P.R. PROCESSING...*",
                    parse_mode="Markdown"
                )
        except Exception as e:
            logger.warning(f"Could not send video: {e}")

    message = SCENARIO_TEMPLATE.format(
        id=selected["id"],
        name=selected["name"],
        description=selected["description"]
    )

    await update.message.reply_text(message, parse_mode="Markdown")


async def list_scenarios(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List all scenario names."""
    log_command(update, "list")

    # Split into chunks to avoid message length limits
    chunk_size = 35
    chunks = [SCENARIOS[i:i + chunk_size] for i in range(0, len(SCENARIOS), chunk_size)]

    for i, chunk in enumerate(chunks):
        start_num = i * chunk_size + 1
        end_num = min((i + 1) * chunk_size, len(SCENARIOS))

        lines = [f"📋 *SCENARIOS {start_num}-{end_num}*\n"]
        for s in chunk:
            lines.append(f"`{s['id']:3d}.` {s['name']}")

        message = "\n".join(lines)
        await update.message.reply_text(message, parse_mode="Markdown")


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random Joshua quote."""
    selected_quote = random.choice(JOSHUA_QUOTES)
    log_command(update, "quote", selected_quote[:30] + "...")

    message = f"""
```
+------------------------------------------+
|            W.O.P.R. OUTPUT               |
+------------------------------------------+
```
*JOSHUA says:*

_{selected_quote}_
"""
    await update.message.reply_text(message, parse_mode="Markdown")


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle unknown commands."""
    await update.message.reply_text(
        "❓ Unknown command. Type /help for available commands.\n\n"
        "_SHALL WE PLAY A GAME?_",
        parse_mode="Markdown"
    )


# ============================================================================
# Main Entry Point
# ============================================================================

def main() -> None:
    """Start the bot."""

    # Replace with your bot token from @BotFather
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("scenario", scenario))
    application.add_handler(CommandHandler("list", list_scenarios))
    application.add_handler(CommandHandler("quote", quote))

    # Start the Bot
    print("🖥️  WOPR ONLINE - SHALL WE PLAY A GAME?")
    print("Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
