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

## Roll Commands

With roll command you can roll dice of specified sizes.
Command input is roll (number)D(number). 
Where the first number is the ammount of dice rolled and the second number is the sides of the dice.
Examples:
```
!roll 5d4
!roll 2D10
```

Extra arguments can be given to make the bot do something with the rolls.
Capitalization does not matter for the arguments.
Curently accepted arguments are:
```
higher, high, h
lower, low, l
under, u
over, o
```
Higest X, gives the highest X rolls.
Lowest X, gives the lowest X rolls.
Under X, gives the rolls that were X or under.
Over X, gives the rolls that were X or over.

Accepted format for the arguments is (argument)(number). Multiple arugments can be given by seperating each one with a (,).
Examples:

```
!roll 10D10 h2, l2,u5,o6
!roll 10d10 low3, high 2, under 2
!roll 10d10 over 7, lowest 5
```

## Work split

Main bot<br />
Felix Pape, Kim Satokangas

Twitter, Blacklist, Converter<br />	
Felix Pape

Youtube, Roller<br />
Kim Satokangas
