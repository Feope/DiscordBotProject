#
# WIP
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv("TWITTER_CONSUMER_TOKEN")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET_TOKEN")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET_TOKEN")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.id)
        print(tweet.text)
    def on_matching_rules(self, matching_rules):
        print('matched rule')
        return super().on_matching_rules(matching_rules)
    def on_connect(self):
        print("connected")
        print(printer.running)
        print(printer.get_rules())
        return super().on_connect()
    def on_exception(self, exception):
        print("excpetion")
        return super().on_exception(exception)
    def on_disconnect(self):
        print("disconnect")
        return super().on_disconnect()

printer = MyStream(bearer_token)

#Remove all existing filter rules
if(printer.get_rules()[0]):
    rulesDeleted = []
    list = printer.get_rules()[0]

    for i in list:
        rulesDeleted.append(i.id)

    for i in rulesDeleted:
        printer.delete_rules(i)

printer.add_rules(tweepy.StreamRule("from:Meisinger2"))
print(printer.get_rules())

printer.filter()
