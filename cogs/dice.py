import random, re

from discord.ext import commands


class DiceRoller(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, input, *, args = None):
        
        #User input should be in form of (number)d(number), ex. 5d10. 
        #Where first number is the number of dice to be rolled and the last number is the sides of the dice.
        #Arguments for optional operations should be seperated with a (,) ex. 5d10 high5, low5, over 2, under 4
        rolls = list()
        argsdict = {}
        argresults = ""
        ucount = 0
        ocount = 0
        try:
            input = input.lower()
            inputpart = input.partition("d")
            rollnum = int(inputpart[0])
            sides = int(inputpart[2])
        except:
            await ctx.send(f"""```fix\nCommand input should be in form of "!roll (number)d(number)", ex. !roll 5d10\nWhere first number is the number of dice to be rolled and the last number is the sides of the dice.\nArguments for optional operations should be seperated with a (,) ex. 5d10 high5, low5, over 2, under 4\n```""")


        try:
            args = args.lower()
            midargs = "".join(args.split())
            separgs = midargs.split(",")
            for i, arg in enumerate(separgs):
                match = re.match(r"([a-z]+)([0-9]+)", arg, re.I)
                tmp = match.groups()
                argsdict[tmp[0]] = int(tmp[1])
        except:
            argresults = "\nArgument error. Try high, low, under or over followed by a number and seperated by ,\nExample, 4d4 high1, low1, over2, under2"
               
        for _ in range (rollnum):
            rolls.append(random.randint(1, sides))

        #if there are no args, skip going through the args block
        if args == None:
            rolls.sort(reverse=True) 
            await ctx.send(f"```fix\nRolling {sides} sided dice {rollnum} times.\nTotal: {sum(rolls)} \nThe rolls were: \n{str(rolls)[1:-1]}\n```")
        
        #Args block
        else:
            if "highest" in argsdict or "high" in argsdict or "h" in argsdict:
                if "highest" in argsdict:
                    hkey = "highest"
                elif "high" in argsdict:
                    hkey = "high"
                else:
                    hkey = "h"
                rolls.sort(reverse=True)
                highrolls = rolls[0:argsdict[hkey]]
                argresults = (f"\nHighest {argsdict[hkey]}: {str(highrolls)[1:-1]}")

            if "lowest" in argsdict or "low" in argsdict or "l" in argsdict:
                if "lowest" in argsdict:
                    lkey = "lowest"
                elif "low" in argsdict:
                    lkey = "low"
                else:
                    lkey = "l"
                rolls.sort()
                lowrolls = rolls[0:argsdict[lkey]]
                argresults = argresults + (f"\nLowest {argsdict[lkey]}: {str(lowrolls)[1:-1]}")

            if "over" in argsdict or "o" in argsdict:
                if "over" in argsdict:
                    okey = "over"
                else:
                    okey = "o"
                for i in rolls:
                    if i >= argsdict[okey]:
                        ocount += 1
                argresults = argresults + (f"\nRolls of {argsdict[okey]} or over: {ocount}")

            if "under" in argsdict or "u" in argsdict:
                if "under" in argsdict:
                    ukey = "under"
                else:
                    ukey = "u"
                for i in rolls:
                    if i <= argsdict[ukey]:
                        ucount += 1
                argresults = argresults + (f"\nRolls of {argsdict[ukey]} or under: {ucount}")

            rolls.sort(reverse=True) 
            await ctx.send(f"```fix\nRolling {sides} sided dice {rollnum} times.\n\nTotal: {sum(rolls)}{argresults}\n\nThe rolls were: \n{str(rolls)[1:-1]}\n```")
        #end of args block
            

#loading the cog to bot
def setup(bot):
    print('Dice roller loaded')
    bot.add_cog(DiceRoller(bot))