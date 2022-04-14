# YouTube Link
import json, os, discord, requests

from discord.ext import commands, tasks
from dotenv import load_dotenv

#fetch Youtube API key from env file
load_dotenv()
YTKEY = os.getenv("YOUTUBE_APITOKEN")
GUILD = os.getenv("DISCORD_GUILD")


class YoutubeWatcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.youtubeid = None
        self.channel = None
        self.oldvid = None

    #starts the background task loop checking for updates
    def ytstart(self):
        self.ytupdates.start()

    #stops the background task loop checking for updates
    def ytstop(self):
        self.ytupdates.cancel()

    #fetch a list of videos on channel and create a list from them
    def fetch_channel_videos(self, limit = None):
        url = f"https://www.googleapis.com/youtube/v3/search?key={YTKEY}&channelId={self.youtubeid}&part=id&order=date"
        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        videos = list()
        vid_data = data["items"]
        #printing the url for test purposes
        print(url)

        #taking the video IDs from the channel data
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
    async def setyoutubeid(self, ctx, *, youtuberid):
        self.youtubeid = youtuberid
        await ctx.send(f"Youtuber ID set to ``{self.youtubeid}``")

    #command to set the discord channel where bot should post new videos
    @commands.command()
    async def setdiscordchannel(self, ctx, *, channelname):
        self.channel = discord.utils.get(ctx.guild.channels, name=channelname)
        await ctx.send(f"Channel set to ``{self.channel}``")
        await self.channel.send("Hello there.")

    #testcommand, on command checks the latest video on specified youtube channel, if the video is new posts it to chosen discord channel, if not informs that there is no new videos
    @commands.command()
    async def checktest(self, ctx):
        videolist = self.fetch_channel_videos(10)
        newvideo = "https://www.youtube.com/watch?v=" + videolist[0]
        await ctx.send(f"Video ID list ``{videolist}``")
        if newvideo == self.oldvid:
            await ctx.send("No new vids")
            return
        else:
            self.oldvid = newvideo
            await self.channel.send(f"Hello there. {newvideo}")
    
    #background loop for checking target channels for new video uploads
    @tasks.loop(seconds=60)
    async def ytupdates(self):
        videolist = self.fetch_channel_videos(10)
        newvideo = "https://www.youtube.com/watch?v=" + videolist[0]
        if newvideo == self.oldvid:
            return
        else:
            self.oldvid = newvideo
            await self.channel.send(f"Hello there. {newvideo}")

    #user command for starting the channel monitoring loop
    @commands.command()
    async def start(self, ctx):
        self.ytstart()
        await ctx.send("Starting monitoring")

    #user command for stopping the channel monitoring loop
    @commands.command()
    async def stop(self, ctx):
        self.ytstop()
        await ctx.send("Stopping monitoring")

#loading the cog to bot
def setup(bot):
    print('YTL commands loaded')
    bot.add_cog(YoutubeWatcher(bot))