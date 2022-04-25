import discord
from discord.ext import commands
import re

class Conversion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Listener when cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Converter loaded")

    #Listener for Temperature Conversion, listening through all messages
    @commands.Cog.listener()
    async def on_message(self, ctx):
        message = ctx.content
        channel = ctx.channel

        #Searching if any message containts number + C
        x = re.search("-*\d+[cC](?:\s*-\d+[cC])?", message)

        #Upon finding someone mentiond a degree in Celsius
        if(x):
            #Taking the result and removing the C
            result = x.group(0)
            trimmed_result = int(result[:-1])

            #Converting Celsius to Fahrenheit and Kelvin
            if(trimmed_result):
                cToF = (trimmed_result * 9/5) + 32
                cToK = trimmed_result + 273.15

            #Creating embed with the results because it looks nicer and sending it
            embed=discord.Embed(title=f"{trimmed_result}C", description=f"{cToF}F and {cToK}K", color=0xFF5733)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Conversion(bot))


