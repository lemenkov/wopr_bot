# 🖥️ SHALL WE PLAY A GAME?

A Telegram bot that serves nuclear war scenarios from the movie [WarGames
(1983)](https://www.imdb.com/title/tt0086567/).

Joshua (WOPR) will share its 140 Global Thermonuclear War scenarios with you.

```
+------------------------------------------+
|    W.O.P.R. - WAR OPERATION PLAN         |
|          RESPONSE SYSTEM                 |
|      CHEYENNE MOUNTAIN COMPLEX           |
+------------------------------------------+
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
3. Copy the bot token

### 2. Install Dependencies

```bash
cd wopr_bot
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
wopr_bot/
├── joshua_bot.py      # Main bot code (MIT License)
├── scenarios.json     # All 140 nuclear war scenarios (Fair Use - see below)
├── wopr.mp4           # WOPR computer animation clip (Fair Use - see below)
├── requirements.txt   # Python dependencies
├── LICENSE            # MIT License for the code
└── README.md          # This file
```

## 💬 Example Output

```
+------------------------------------------+
|  GLOBAL THERMONUCLEAR WAR SCENARIO #011  |
+------------------------------------------+
```
**SEATO Decapitating**

SEATO dissolved in 1977. A decapitation attack would have been nuclear strikes
against the capital cities of its member-states.

*WINNER: NONE*

## 🎬 About WarGames (1983)

[WarGames](https://www.imdb.com/title/tt0086567/) is a 1983 American
techno-thriller film starring Matthew Broderick as David Lightman, a young
hacker who accidentally accesses WOPR (War Operation Plan Response), a United
States military supercomputer programmed to simulate nuclear war scenarios.

In the film's climax, WOPR/Joshua cycles through all 140+ nuclear war
scenarios, learning that they all result in mutual destruction, leading to the
famous conclusion:

> *"A STRANGE GAME. THE ONLY WINNING MOVE IS NOT TO PLAY."*
> 
> *"HOW ABOUT A NICE GAME OF CHESS?"*

## 📚 Scenario Sources

The scenario descriptions are based on Cold War analysis from:
- [WW31987 WordPress Blog](https://ww31987.wordpress.com/)

## ⚖️ License & Fair Use

### Code (MIT License)

The bot source code (`joshua_bot.py`, `requirements.txt`) is released under the
[MIT License](LICENSE). You are free to use, modify, and distribute it.

### Movie Content (Fair Use)

The following files contain content from [WarGames
(1983)](https://www.imdb.com/title/tt0086567/) and are included under [Fair
Use](https://en.wikipedia.org/wiki/Fair_use) doctrine for purposes of
commentary, education, and fan appreciation:

- **`scenarios.json`** — List of nuclear war scenario names visible in the
  film, with educational descriptions explaining their Cold War context
- **`wopr.mp4`** — Brief clip of the WOPR computer display from the film

This is a non-commercial fan project. The film WarGames is © 1983 MGM/UA
Entertainment.  All trademarks belong to their respective owners.

## ⚠️ Disclaimer

This is a fan project for entertainment and educational purposes. The scenarios
are fictional and from a 1983 movie. This bot is not affiliated with MGM, the
filmmakers, or any military organization.

---

*"The only winning move is not to play."* — Joshua, 1983
