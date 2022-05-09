import discord
from discord.ext import commands
import re

#List object for the black listed words
bList = []

#Open the file where the listed words are saved
f = open("list.txt", "r")
bList = f.read().split(", ")
f.close()

#Blacklist Cog
class Blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Listener for the backlisted words
    @commands.Cog.listener()
    async def on_message(self, ctx):
        message = ctx.content

        #Only non admins messages get deleted
        if not(discord.utils.get(ctx.author.roles, name='Admin')):
            if any(x in message for x in bList):
                print("match")
                await ctx.delete()

    #Include new word/string in the list, but only admins
    @commands.command(name="include")
    @commands.has_permissions(administrator=True)
    async def include(self, ctx):
        message = ctx.message.content

        #remove the "!include " part
        newMatch = message[9:]

        #Append the string the list
        bList.append(newMatch)

        #Substitute \ and [ ] 
        result = str(bList)
        result = re.sub('[\[\]\']', '', result)

        #Write the changes to the file
        f = open("list.txt", "w")
        f.write(result)
        f.close()

    #Remove a word/string from the list, but only admins
    @commands.command(name="exclude")
    @commands.has_permissions(administrator=True)
    async def exclude(self, ctx):
        message = ctx.message.content
        channel = ctx.channel

        #remove the "!exclude " part
        newMatch = message[9:]

        #Check if the string is contained in the list
        if newMatch in bList:
            bList.remove(newMatch)

            #Substitute \ and [ ] 
            result = str(bList)
            result = re.sub('[\[\]\']', '', result)

            #Write the changes to the file
            f = open("list.txt", "w")
            f.write(result)
            f.close()
        else:
            await channel.send('No such word in the blacklist')

def setup(bot):
    bot.add_cog(Blacklist(bot))