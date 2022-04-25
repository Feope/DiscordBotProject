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

    @commands.command()
    async def convert(self, ctx):
        message = ctx.message.content
        channel = ctx.channel
        print(f'{message}1')
        result = message[8:]

        if(result):
            trimmedResult = re.sub(r'[0-9\.\s]+', '', result)
            resultLower = trimmedResult.lower()
            numberResult = re.sub(r'[\D\s]+', '', result)
            metres = 0

            if(resultLower == 'm'):
                await channel.send('metre')
                metres = int(numberResult)
            elif(resultLower == 'km'):
                await channel.send('kilometre')
                metres = int(numberResult) * (10**3)
            elif(resultLower == 'dm'):
                await channel.send('decimetre')
                metres = int(numberResult) * (10**-1)
            elif(resultLower == 'cm'):
                await channel.send('centimetre')
                metres = int(numberResult) * (10**-2)
            elif(resultLower == 'mm'):
                await channel.send('millimetre')
                metres = int(numberResult) * (10**-3)
            elif(resultLower == 'inches'):
                await channel.send('millimetre')
                metres = int(numberResult) * 0.0254
            elif(resultLower == 'miles'):
                await channel.send('millimetre')
                metres = int(numberResult) * 1609.344
            elif(resultLower == 'feet'):
                await channel.send('millimetre')
                metres = int(numberResult) * 0.3048

            km = metres * (10**-3)
            m = metres
            dm = metres * (10**1)
            cm = metres * (10**2)
            mm = metres * (10**3)
            miles = metres * 0.0006213712
            feet = metres * 3.280839895
            inches = metres * 39.3700787402

            embed=discord.Embed(title=f"{result}", description=f"{km}km {m}m {dm}dm {cm}cm {mm}mm\n {miles}miles {feet}feet {inches}inches", color=0xFF5733)
            await channel.send(ctx.author.mention, embed=embed)

    #Listener for Temperature Conversion, listening through all messages
    @commands.Cog.listener()
    async def on_message(self, ctx):
        message = ctx.content
        channel = ctx.channel

        #Searching if any message containts number + C
        x = re.search("-*\d+[cC](?:\s*-\d+[cC])?(\Z|\s)", message)

        #Upon finding someone mentiond a degree in Celsius
        if(x):
            #Taking the result and removing the C
            result = x.group(0)
            trimmed_result = int(re.sub('\D', '', result))

            #Converting Celsius to Fahrenheit and Kelvin
            if(trimmed_result):
                cToF = (trimmed_result * 9/5) + 32
                cToK = trimmed_result + 273.15

            #Creating embed with the results because it looks nicer and sending it
            embed=discord.Embed(title=f"{trimmed_result}F", description=f"{cToF}F and {cToK}K", color=0xFF5733)
            await channel.send(embed=embed)
        else:
            y = re.search("-*\d+[fF](?:\s*-\d+[fF])?(\Z|\s)", message)
            if(y):
                #Taking the result and removing the F
                result = y.group(0)
                trimmed_result = int(re.sub('\D', '', result))

                #Converting Fahrenheit to Celsius and Kelvin
                if(trimmed_result):
                    fToC = (trimmed_result - 32) * 5/9
                    fToK = trimmed_result + 273.15

                #Creating embed with the results because it looks nicer and sending it
                embed=discord.Embed(title=f"{trimmed_result}C", description=f"{fToC}C and {fToK}K", color=0xFF5733)
                await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Conversion(bot))