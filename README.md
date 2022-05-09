# DiscordBotProject
A bot for learning purposes that can convert units, automatically delete messages containing specified words, roll dice and notify about new YouTube videos.


## Requirements
```bash
pip install discord.py
pip install python-dotenv
pip install regex
pip install --upgrade google-api-python-client
pip install --upgrade google-auth-oauthlib google-auth-httplib2
```

Register a bot by following the guide in the [Discord Developer Portal](https://discord.com/developers/docs/getting-started) and add it to your server.

Create a .env file and add your token from the registered bot:
```bash
DISCORD_TOKEN="TOKEN HERE"
```

## Usage
All available commands can be accessed by default by typing `!help`

For the blacklist you may edit the list.txt manually like this:

```
bad, test, words, reversed
```
