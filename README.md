# Discord DDNet Stats Bot

This is a Discord bot that retrieves and displays player statistics for the game DDNet (Dexter's DDrace Network). It allows users to view detailed statistics about their gameplay, including time spent in different game modes and overall points, and visualizes this data in a pie chart.

## Features

- Fetches player statistics from the DDNet API
- Displays a pie chart of the player's game time by mode
- Provides information such as clan and points
- Built with Disnake for interaction with the Discord API

## Prerequisites

- Python 3.11 or higher
- A Discord bot token (create one via the [Discord Developer Portal](https://discord.com/developers/applications))
- Install the required Python libraries:
  - `disnake`
  - `aiohttp`
  - `matplotlib`
  - `python-dotenv`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discord-game-stats-bot.git
   cd discord-game-stats-bot
   ```

2. **Create a `.env` file** in the root directory and add your Discord bot token:

   ```plaintext
   TOKEN=your_discord_bot_token_here
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the bot:**

   ```bash
   python bot.py
   ```

2. **Invite your bot to your Discord server** using the OAuth2 URL generated in the Discord Developer Portal.

3. **Use the `/stats` command** in Discord to retrieve player statistics. For example:

   ```
   /stats <PlayerName>
   ```

   This command will return the player's statistics along with a pie chart showing the distribution of time spent in different game modes.
