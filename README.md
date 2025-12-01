# 🖥️ SHALL WE PLAY A GAME?

A Telegram bot that serves nuclear war scenarios from the movie **WarGames (1983)**.

Joshua (WOPR) will share its 140 Global Thermonuclear War scenarios with you.

```
╔══════════════════════════════════════════╗
║     W.O.P.R.  -  WAR OPERATION PLAN     ║
║              RESPONSE SYSTEM             ║
║         CHEYENNE MOUNTAIN COMPLEX        ║
╚══════════════════════════════════════════╝
```

## 📋 Features

- `/start` - Greet the user (Joshua style)
- `/help` - Show available commands
- `/scenario` - Get a random nuclear war scenario
- `/scenario <number>` - Get a specific scenario (1-140)
- `/list` - List all 140 scenario names
- `/quote` - Get Joshua's famous quotes

## 🚀 Quick Start

### 1. Get a Telegram Bot Token

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow the prompts
3. Copy the bot token (looks like `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 2. Install Dependencies

```bash
cd wargames_bot
pip install -r requirements.txt
```

### 3. Configure the Bot

Edit `joshua_bot.py` and replace `YOUR_BOT_TOKEN_HERE` with your actual token:

```python
BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
```

### 4. Run the Bot

```bash
python joshua_bot.py
```

You should see:
```
🖥️  WOPR ONLINE - SHALL WE PLAY A GAME?
Press Ctrl+C to stop.
```

## 📁 Files

```
wargames_bot/
├── joshua_bot.py      # Main bot code
├── scenarios.json     # All 140 nuclear war scenarios
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## 💬 Example Output

```
╔══════════════════════════════════════════╗
║  GLOBAL THERMONUCLEAR WAR SCENARIO #011  ║
╠══════════════════════════════════════════╣
║          SEATO Decapitating              ║
╚══════════════════════════════════════════╝

📋 SEATO Decapitating

SEATO dissolved in 1977. A decapitation attack would have been
nuclear strikes against the capital cities of its member-states.

WINNER: NONE
```

## 🎬 About WarGames (1983)

WarGames is a 1983 American techno-thriller film starring Matthew Broderick
as David Lightman, a young hacker who accidentally accesses WOPR (War Operation
Plan Response), a United States military supercomputer programmed to simulate
nuclear war scenarios.

In the film's climax, WOPR/Joshua cycles through all 140+ nuclear war scenarios,
learning that they all result in mutual destruction, leading to the famous
conclusion:

> *"A STRANGE GAME. THE ONLY WINNING MOVE IS NOT TO PLAY."*
> *"HOW ABOUT A NICE GAME OF CHESS?"*

## 📚 Scenario Sources

The scenario descriptions are based on analysis from:
- [WW31987 WordPress Blog](https://ww31987.wordpress.com/) - Cold War analysis

## ⚠️ Disclaimer

This is a fan project for entertainment purposes. The scenarios are fictional
and from a 1983 movie. The bot is not affiliated with MGM, the filmmakers,
or any military organization.

---

*"The only winning move is not to play."* - Joshua, 1983
