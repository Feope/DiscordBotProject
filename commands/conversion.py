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

    @commands.command(name="convert", aliases=["c"])
    async def convert(self, ctx):
        message = ctx.message.content
        channel = ctx.channel
        if(message.startswith("co")):
            result = message[8:]
        else:
            result = message[2:]

        if(result):
            trimmedResult = re.sub(r'[0-9\.\s]+', '', result)
            resultLower = trimmedResult.lower()
            numberResult = re.sub(r'[\D\s]+', '', result)
            metres = 0

            if(resultLower == 'm'):
                metres = int(numberResult)
            elif(resultLower == 'km'):
                metres = int(numberResult) * (10**3)
            elif(resultLower == 'dm'):
                metres = int(numberResult) * (10**-1)
            elif(resultLower == 'cm'):
                metres = int(numberResult) * (10**-2)
            elif(resultLower == 'mm'):
                metres = int(numberResult) * (10**-3)
            elif(resultLower == 'inches'):
                metres = int(numberResult) * 0.0254
            elif(resultLower == 'miles'):
                metres = int(numberResult) * 1609.344
            elif(resultLower == 'feet'):
                metres = int(numberResult) * 0.3048

            km = round(metres * (10**-3), 3)
            m = round(metres, 3)
            dm = round(metres * (10**1), 3)
            cm = round(metres * (10**2), 3)
            mm = round(metres * (10**3), 3)
            miles = round(metres * 0.0006213712, 3)
            feet = round(metres * 3.280839895, 3)
            inches = round(metres * 39.3700787402, 3)

            if(km == 0):
                km = "<0.001"
            if(m == 0):
                m = "<0.001"
            if(dm == 0):
                dm = "<0.001"
            if(cm == 0):
                cm = "<0.001"
            if(mm == 0):
                mm = "<0.001"
            if(miles == 0):
                miles = "<0.001"
            if(feet == 0):
                feet = "<0.001"
            if(inches == 0):
                inches = "<0.001"

            embed=discord.Embed(title=f"{result}", color=0xFF5733)
            embed.add_field(name="km", value=f"{km}", inline=True)
            embed.add_field(name="m", value=f"{m}", inline=True)
            embed.add_field(name="dm", value=f"{dm}", inline=True)
            embed.add_field(name="cm", value=f"{cm}", inline=True)
            embed.add_field(name="mm", value=f"{mm}", inline=True)
            embed.add_field(name="miles", value=f"{miles}", inline=True)
            embed.add_field(name="feet", value=f"{feet}", inline=True)
            embed.add_field(name="inches", value=f"{inches}", inline=True)
            embed.set_footer(text="Values rounded to 3 digits after the decimal point")
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
            trimmed_result = int(re.sub('[a-zA-Z]', '', result))

            #Converting Celsius to Fahrenheit and Kelvin
            if(trimmed_result):
                cToF = round((trimmed_result * 9/5) + 32, 3)
                cToK = round(trimmed_result + 273.15, 3)

            #Creating embed with the results because it looks nicer and sending it
            embed=discord.Embed(title=f"{trimmed_result}C", color=0xFF5733)
            embed.add_field(name="Fahrenheit", value=f"{cToF}", inline=True)
            embed.add_field(name="Kelvin", value=f"{cToK}", inline=True)
            embed.set_footer(text="Values rounded to 3 digits after the decimal point")
            await channel.send(embed=embed)
        else:
            y = re.search("-*\d+[fF](?:\s*-\d+[fF])?(\Z|\s)", message)
            if(y):
                #Taking the result and removing the F
                result = y.group(0)
                trimmed_result = int(re.sub('[a-zA-Z]', '', result))

                #Converting Fahrenheit to Celsius and Kelvin
                if(trimmed_result):
                    fToC = round((trimmed_result - 32) * 5/9, 3)
                    fToK = round(trimmed_result + 273.15, 3)

                #Creating embed with the results because it looks nicer and sending it
                embed=discord.Embed(title=f"{trimmed_result}F", color=0xFF5733)
                embed.add_field(name="Celsius", value=f"{fToC}", inline=True)
                embed.add_field(name="Kelvin", value=f"{fToK}", inline=True)
                embed.set_footer(text="Values rounded to 3 digits after the decimal point")
                await channel.send(embed=embed)
            else:
                z = re.search("-*\d+[kK](?:\s*-\d+[kK])?(\Z|\s)", message)
                if(z):
                    #Taking the result and removing the F
                    result = z.group(0)
                    trimmed_result = int(re.sub('[a-zA-Z]', '', result))

                    #Converting Fahrenheit to Celsius and Kelvin
                    if(trimmed_result):
                        kToC = round((trimmed_result - 273.15) * 5/9, 3)
                        kToF = round((trimmed_result - 273.15) * (9/5) + 32, 3)

                    #Creating embed with the results because it looks nicer and sending it
                    embed=discord.Embed(title=f"{trimmed_result}K", color=0xFF5733)
                    embed.add_field(name="Celsius", value=f"{kToC}", inline=True)
                    embed.add_field(name="Fahrenheit", value=f"{kToF}", inline=True)
                    embed.set_footer(text="Values rounded to 3 digits after the decimal point")
                    await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Conversion(bot))