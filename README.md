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

Create a Youtube API key by following the guide to create API keys in [Google Developers documentation](https://developers.google.com/youtube/registering_an_application)

Create a .env file and add your tokens from the registered bot and youtube:
```bash
DISCORD_TOKEN="TOKEN HERE"
YOUTUBE_APITOKEN=”TOKEN HERE”
```

## Usage
All available commands can be accessed by default by typing `!help`

For the blacklist you may edit the list.txt manually like this:

```
bad, test, words, reversed
```

## Roll Commands

With roll command you can roll dice of specified sizes.<br />
Command input is roll (number)D(number).<br /> 
Where the first number is the ammount of dice rolled and the second number is the sides of the dice.<br />
Examples:
```
!roll 5d4
!roll 2D10
```

Extra arguments can be given to make the bot do something with the rolls.<br />
Capitalization does not matter for the arguments.<br />
Curently accepted arguments are:
```
higher, high, h
lower, low, l
under, u
over, o
```
Higest X, gives the highest X rolls.<br />
Lowest X, gives the lowest X rolls.<br />
Under X, gives the rolls that were X or under.<br />
Over X, gives the rolls that were X or over.<br />

Accepted format for the arguments is (argument)(number). Multiple arugments can be given by seperating each one with a (,).<br />
Examples:

```
!roll 10D10 h2, l2,u5,o6
!roll 10d10 low3, high 2, under 2
!roll 10d10 over 7, lowest 5
```
## Youtube Commands

Bot can be set to monitor a Youtube channel and post new uploads to a specified discord channel periodically.<be />
Currently recognized commands are:

```
ythelp X
```
Gives information about the given command X. Where X is one of the other Youtube commands.

```
setdiscordchannel
```
Sets the channel bot will use to send notifications to.
```
setyoutubeid
```
Sets the Youtube channel id, which the bot will use to check for uploads.
```
checktest
```
Test command to see if the bot is working correctly.

```
start
stop
```
Commands to start and stop the monitoring loop.

## Work split

Main bot<br />
Felix Pape, Kim Satokangas

Twitter, Blacklist, Converter<br />	
Felix Pape

Youtube, Roller<br />
Kim Satokangas
