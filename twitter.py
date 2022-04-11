#
#
import os
import tweepy
import json
from dotenv import load_dotenv

#Loading the authentication token for the bot
load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

#Url snippets to recreate the link for the tweet
base_url = "https://twitter.com/"
url_tag = ""
url_part2 = "/status/"
url_id = ""

#Variables that will contain the link, text and author of the tweet
tweet_text = ""
tweet_author = url_tag
url = ""

def twitter_bot():
    class MyStream(tweepy.StreamingClient):

        #Receives the tweet data
        def on_data(self, raw_data):
            #Raw data is in byte format so it's decoded first
            decoded_data = raw_data.decode('UTF-8')
            #Load the string as json
            json_data = json.loads(decoded_data)

            #Extract id, name and text from the json
            tweet_id = json_data["data"]["id"]
            tweet_text = json_data["data"]["text"]
            tweet_author_from_rules = json_data["matching_rules"][0]["tag"]

            #Access global variables
            global base_url
            global url_tag
            global url_part2
            global url_id
            global url

            #Assign the tag and id to the global variables
            url_tag = tweet_author_from_rules
            url_id = tweet_id

            #Recreate the link to the tweet using author from the tag and tweet id
            url = f"{base_url}{url_tag}{url_part2}{url_id}"

            print(f"ID, Text and name from rule tags: {tweet_id} {tweet_text} {tweet_author_from_rules}")
            print(f"Link to the tweet: {url}")
            print(tweet_text)

            return super().on_data(raw_data)

        #Print connected and True in console to know when it is ready to handle tweets    
        def on_connect(self):
            print("connected")
            print(printer.running)
            return super().on_connect()

        #Print exception or disconnect on exception or disconnect    
        def on_exception(self, exception):
            print("excpetion")
            return super().on_exception(exception)
        def on_disconnect(self):
            print("disconnect")
            return super().on_disconnect()

    #Assign the token and to wait if limit is reached 
    printer = MyStream(bearer_token, wait_on_rate_limit=True)

    #Remove all existing filter rules
    if(printer.get_rules()[0]):
        rulesDeleted = []
        list = printer.get_rules()[0]

        for i in list:
            rulesDeleted.append(i.id)

        for i in rulesDeleted:
            printer.delete_rules(i)

    #Rules to filter for person
    printer.add_rules(tweepy.StreamRule("from:Meisinger2", "Meisinger2"))

    printer.filter()