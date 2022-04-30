import random, re

from discord.ext import commands


class DiceRoller(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, input, *, args = None):
        
        #User input should be in form of (number)d(number), ex. 5d10. 
        #Where first number is the number of dice to be rolled and the last number is the sides of the dice.


        input = input.lower()
        inputpart = input.partition("d")
        rollnum = int(inputpart[0])
        sides = int(inputpart[2])
        rolls = list()
        argsdict = {}
        optional = ""

        try:
            args = args.lower()
            midargs = "".join(args.split())
            separgs = midargs.split(",")
            for i, arg in enumerate(separgs):
                match = re.match(r"([a-z]+)([0-9]+)", arg, re.I)
                tmp = match.groups()
                argsdict[tmp[0]] = tmp[1]
        except:
            optional = "error"
               
        for _ in range (rollnum):
            rolls.append(random.randint(1, sides))

        if args == None:
            await ctx.send(f"Rolling {sides} sided dice {rollnum} times.\nTotal: {sum(rolls)} \nThe rolls are: \n{str(rolls)[1:-1]}")

        else:
            if "highest" in argsdict or "high" in argsdict or "h" in argsdict:
                optional = "H-trig"
            if "lowest" in argsdict or "low" in argsdict or "l" in argsdict:
                optional = optional + "L-trig, "
            if "under" in argsdict or "u" in argsdict:
                optional = optional + "U-trig, "
            if "over" in argsdict or "o" in argsdict:
                optional = optional + "O-trig, "   

            await ctx.send(f"Rolling {sides} sided dice {rollnum} times.\nTotal: {sum(rolls)} \nThe results are: {str(rolls)[1:-1]}\n{argsdict}\n{optional}")
            

#loading the cog to bot
def setup(bot):
    print('Dice roller loaded')
    bot.add_cog(DiceRoller(bot))