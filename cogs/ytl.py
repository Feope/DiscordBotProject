# YouTube Link
import json, os, discord, requests, traceback

from discord.ext import commands, tasks
from dotenv import load_dotenv

#fetch Youtube API key from env file
load_dotenv()
YTKEY = os.getenv("YOUTUBE_APITOKEN")

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
        print(url)#printing the url for test purposes
        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        videos = list()
        vid_data = data["items"]

        #taking the video IDs from the channel data
        for item in vid_data:
            try:
                kind = item["id"]["kind"]
                if kind == "youtube#video":
                    video_id = item["id"]["videoId"]
                    videos.append(video_id)
            except KeyError:
                print("KeyError")
        return videos

    #command to set the youtube channels ID 
    @commands.command()
    async def setyoutubeid(self, ctx, *, youtuberid):

        url = f"https://www.googleapis.com/youtube/v3/search?key={YTKEY}&channelId={youtuberid}&part=snippet"
        print(url) #printing the url for test purposes
        try:
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            channelname = data['items'][0]['snippet']['channelTitle']
            self.youtubeid = youtuberid
            await ctx.send(f"Youtuber ID set to ``{self.youtubeid}`` \nChannel name is {channelname}")
        except:
            await ctx.send("Invalid channel or the channel is empty")

    #command to set the discord channel where bot should post new videos
    @commands.command()
    async def setdiscordchannel(self, ctx, *, channelname):
        try:
            self.channel = discord.utils.get(ctx.guild.channels, name=channelname)
            if self.channel != None:
                await ctx.send(f"Channel set to ``{self.channel}``")
            await self.channel.send("Channel set.")
        except:
            await ctx.send(f"Channel not found, channel set to ``{self.channel}``")

    #testcommand, on command checks the latest video on specified youtube channel, if the video is new posts it to chosen discord channel, if not informs that there is no new videos
    @commands.command()
    async def checktest(self, ctx):
        if (self.channel != None and self.youtubeid != None):
            videolist = self.fetch_channel_videos(10)
            newvideo = "https://www.youtube.com/watch?v=" + videolist[0]
            await ctx.send(f"Video ID list ``{videolist}``")
            if newvideo == self.oldvid:
                await ctx.send("No new vids")
                return
            else:
                self.oldvid = newvideo
                await self.channel.send(f"Hello there. {newvideo}")
        elif self.channel != None:
            await ctx.send(f"Youtube channel ID not set.")
        elif self.youtubeid != None:
            await ctx.send(f"Discord channel not set.")
        else:
            await ctx.send(f"Discord channel & youtube channel ID not set.")
    
    #background loop for checking target channel for new video uploads
    @tasks.loop(minutes=15)
    async def ytupdates(self):
        try:
            videolist = self.fetch_channel_videos(10)
            newvideo = "https://www.youtube.com/watch?v=" + videolist[0]
            if newvideo == self.oldvid:
                return
            else:
                self.oldvid = newvideo
                await self.channel.send(f"Hello there. {newvideo}")
        except Exception:
            print("There was an error")
            print(traceback.format_exc())
            

    #user command for starting the channel monitoring loop
    @commands.command()
    async def start(self, ctx):
        if self.channel != None and self.youtubeid != None:
            self.ytstart()
            await ctx.send("Starting monitoring")
        elif self.channel != None:
            await ctx.send(f"Youtube channel ID not set.")
        elif self.youtubeid != None:
            await ctx.send(f"Discord channel not set.")
        else:
            await ctx.send(f"Discord channel & youtube channel ID not set.")


    #user command for stopping the channel monitoring loop
    @commands.command()
    async def stop(self, ctx):
        self.ytstop()
        await ctx.send("Stopping monitoring")
    
    #Help command to explain what other commands do
    @commands.command()
    async def ythelp(self, ctx, *args):
        match args:
            case args if "setyoutubeid" in args:
                await ctx.send("""```setyoutubeid```This command is used to set the youtube channel ID the bot will monitor for uploads.
Youtube channel ID is the long string for characters that comes after /channel/ in the browser adress bar.
```youtube.com/channel/UC2qctq0C3AjymJHMQAONMbQ``` Channel ID for this channel would be "UC2qctq0C3AjymJHMQAONMbQ" """)
            case args if "setdiscordchannel" in args:
                await ctx.send("""```setdiscordchannel```This command is used to set the discord channel where the bot will post new uploads it detects on the target youtube channel.
The chosen channel needs to exist on the server and the name needs to be written in correct case.""")
            case args if "checktest" in args:
                await ctx.send("""```checktest``` This command is used to test the video fetching from the channel and to see if everything is set up correctly.""")
            case args if "start" in args or "stop" in args:
                await ctx.send("""```start``` and ```stop``` Start command will begin the monitoring of the chosen channel. Stop command will stop the monitoring.""")
            case _:
                await ctx.send("""Write a YT command after the help command to get information about the given command.
The commands are: setyoutubeid, setdiscordchannel, checktest, start, stop.""")
            

#loading the cog to bot
def setup(bot):
    print('YTL commands loaded')
    bot.add_cog(YoutubeWatcher(bot))