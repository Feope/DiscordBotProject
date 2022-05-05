import discord
from discord.ext import commands
import re

bList = []

def readFile():
    f = open("myfile.txt", "r")
    bList = f.read().split(", ")
    print(bList[1])

def appendToList():
    bList.append('4')
    print(bList)

def writeToFile():
    result = str(bList)
    result = re.sub('[\[\]\']', '', result)
    print(result)

    f = open("myfile.txt", "w")
    f.write(result)

class Blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

if __name__ == "__main__":
    readFile()