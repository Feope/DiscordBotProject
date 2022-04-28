import random

from discord.ext import commands


class DiceRoller(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, input, *, args = None):
        
        #User input should be in form of (number)d(number), ex. 5d10. 
        #Where first number is the number of dice to be rolled and the last number is the sides of the dice.

        inputpart = input.partition("d")
        rolls = list()
        rollnum = int(inputpart[0])
        sides = int(inputpart[2])

        for _ in range (rollnum):
            rolls.append(random.randint(1, sides))

        if args == None:
            await ctx.send(f"Rolling {inputpart[2]} sided dice {inputpart[0]} times. \nThe results are: {str(rolls)[1:-1]}")
        else:
            await ctx.send(f"Rolling {inputpart[2]} sided dice {inputpart[0]} times. \nThe results are: {str(rolls)[1:-1]}\n{args}")
            #todo args block for different options



#loading the cog to bot
def setup(bot):
    print('Dice roller loaded')
    bot.add_cog(DiceRoller(bot))