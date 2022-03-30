# bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()

#botcommand block
botprefix = '!'
def botcurrentprefix(): return botprefix + 'prefix'
def botsetprefix(): return botprefix + 'set'
def botgreet(): return botprefix + 'greet'
def bothelp(): return botprefix + 'help'
#end of botcommand block

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
@client.event
async def on_message(message):
    global botprefix
    channel = message.channel
    mauth = message.author
    match message:
        case botcommand if botcommand.content.startswith(botcurrentprefix()) == True: #botcurrent prefix
            await channel.send('Current botcommand prefix is ' + str(botprefix))

        case botcommand if botcommand.content.startswith(botgreet()) == True: #botgreet
            await channel.send('Hello ' + str(mauth))

        case botcommand if botcommand.content.startswith(botsetprefix()) == True: #botsetprefix
            msg = message.content
            botprefix = msg[-1]
            await channel.send('New botcommand prefix is ' +str(botprefix))
            return botprefix

        case botcommand if botcommand.content.startswith(bothelp()) == True: #bothelp
            await channel.send(
                'Current commands for the bot are: \n' +
                botcurrentprefix() + '\n' +
                botsetprefix() + '\n' +
                botgreet() + '\n' +
                bothelp() + '\n'
            )

client.run(TOKEN)