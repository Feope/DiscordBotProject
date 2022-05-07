# bot.py
import os
import discord

#Environemnt variables to access the token
from dotenv import load_dotenv

#Importing commands for functionality
from discord.ext import commands

#Loading token and guild name to make sure that the correct guild and token are used
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

#Defining prefix for later use in commands
default_prefix = ['!']

#Assigning the prefix to the bot object and turning off the default help command
bot = commands.Bot(command_prefix = default_prefix, help_command=None)

#Event for on launch check if the selected guild from environments is also in the server list.
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

#Printing bot-id and server-id to console
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#Setting the new prefix to passed argument
@bot.command()
async def setprefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f"Prefix changed to ``{prefix}``")

#Send the current prefix(for some reason)
@bot.command()
async def prefix(ctx):
    listToStr = ''.join(map(str, default_prefix))
    await ctx.send(f"Current prefix is ``{listToStr}``")

#Says hello to the user
@bot.command()
async def greet(ctx):
    await ctx.send(f"Hello {ctx.author.display_name}")

#Lists the current commands(manually added) and pings mentioned user(s) or author if no mentions
@bot.command()
async def help(ctx):
    listToStr = ''.join(map(str, bot.command_prefix))
    ping_element = []
    if(ctx.message.mentions):
        for m in ctx.message.raw_mentions:
            pingable = f"<@{m}>"
            ping_element.append(pingable)
            listPing = ' '.join(map(str, ping_element))
        await ctx.send(f"{listPing} Current commands for the bot are: \n" +
                        f"{listToStr}prefix\n" +
                        f"{listToStr}setprefix\n" +
                        f"{listToStr}greet\n" +
                        f"{listToStr}help\n" +
                        f"{listToStr}include(Admin)\n" +
                        f"{listToStr}exclude(Admin)\n" +
                        f"{listToStr}convert\n" +
                        f"{listToStr}c")
    else:
        meauth = f"<@{ctx.author.id}>"    
        await ctx.send(f"{meauth} Current commands for the bot are: \n" +
                        f"{listToStr}prefix\n" +
                        f"{listToStr}setprefix\n" +
                        f"{listToStr}greet\n" +
                        f"{listToStr}help\n" +
                        f"{listToStr}include(Admin)\n" +
                        f"{listToStr}exclude(Admin)\n" +
                        f"{listToStr}convert\n" +
                        f"{listToStr}c")

#Loading extensions/cogs here

#Unit Converter extension
bot.load_extension('commands.conversion')
#Blacklist extension
bot.load_extension('commands.list')

#Run bot using the token
bot.run(TOKEN)