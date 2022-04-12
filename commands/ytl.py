# YouTube Link
import json, os, discord, requests

from discord.ext import commands
from dotenv import load_dotenv

#fetch Youtube API key from env file
load_dotenv()
YTKEY = os.getenv("YOUTUBE_APITOKEN")
GUILD = os.getenv("DISCORD_GUILD")

youtuber = None
channel = None
oldvid = None

#fetch a list of videos on channel and create a list from them
def fetch_channel_videos(limit = None):
    global youtuber
    url = f"https://www.googleapis.com/youtube/v3/search?key={YTKEY}&channelId={youtuber}&part=id&order=date"
    if limit is not None and isinstance(limit, int):
        url += "&maxResults=" + str(limit)
    json_url = requests.get(url)
    data = json.loads(json_url.text)
    videos = list()
    vid_data = data["items"]
    #printing the url for test purposes
    print(url)

    for item in vid_data:
        try:
            kind = item["id"]["kind"]
            if kind == "youtube#video":
                video_id = item["id"]["videoId"]
                videos.append(video_id)
        except KeyError:
            print("error")
    return videos


#command to set the youtube channels ID
@commands.command()
async def setyoutubeid(ctx, *, youtuberid):
    global youtuber
    youtuber = youtuberid
    await ctx.send(f"Youtuber ID set to ``{youtuber}``")

#command to set the discord channel where bot should post new videos
@commands.command()
async def setdiscordchannel(ctx, *, channelname):
    global channel
    channel = discord.utils.get(ctx.guild.channels, name=channelname)
    await ctx.send(f"Channel set to ``{channel}``")
    await channel.send("Hello there.")

#testcommand, on command checks the latest video on specified youtube channel, if the video is new posts it to chosen discord channel, if not informs that there is no new videos
@commands.command()
async def checktest(ctx):
    global channel
    global oldvid
    videolist = fetch_channel_videos(10)
    newvideo = "https://www.youtube.com/watch?v=" + videolist[0]
    await ctx.send(f"Video ID list ``{videolist}``")
    if newvideo == oldvid:
        await ctx.send("No new vids")
        return
    else:
        oldvid = newvideo
        await channel.send(f"Hello there. {newvideo}")



def setup(bot):
    print('ytl')
    bot.add_command(setyoutubeid)
    bot.add_command(setdiscordchannel)
    bot.add_command(checktest)