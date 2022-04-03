# bot.py
import os
import discord

#Environemnt variables to access the token
from dotenv import load_dotenv

#Loading token and guild name to make sure that the correct guild and token are used
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

#Creating the client object that is used to respond to events
client = discord.Client()

#botcommand block
botprefix = '!'
def botcurrentprefix(): return botprefix + 'prefix'
def botsetprefix(): return botprefix + 'set'
def botgreet(): return botprefix + 'greet'
def bothelp(): return botprefix + 'help'

#Event for on launch check if the selected guild from environments is also in the server list.
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

#Printing bot-id and server-id to console
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
#Event for any messages sent       
@client.event
async def on_message(message):

    #Defining channel and author of message for quicker access as well as the prefix
    global botprefix
    channel = message.channel
    mauth = message.author

    #Validating that message is from actual user, ignoring any bots
    if mauth.bot == False:

        #Matching for the botcommands
        match message:

            #User wants to know current prefix
            case botcommand if botcommand.content.startswith(botcurrentprefix()) == True: #botcurrent prefix
                await channel.send('Current botcommand prefix is ' + str(botprefix))

            #User greets
            case botcommand if botcommand.content.startswith(botgreet()) == True: #botgreet
                await channel.send('Hello ' + str(mauth))

            #User wants to change prefix
            case botcommand if botcommand.content.startswith(botsetprefix()) == True: #botsetprefix
                msg = message.content
                botprefix = msg[-1]
                await channel.send('New botcommand prefix is ' +str(botprefix))
                return botprefix

            #User wants to know commands
            case botcommand if botcommand.content.startswith(bothelp()) == True: #bothelp
                await channel.send(
                    'Current commands for the bot are: \n' +
                    botcurrentprefix() + '\n' +
                    botsetprefix() + '\n' +
                    botgreet() + '\n' +
                    bothelp() + '\n'
                )

client.run(TOKEN)