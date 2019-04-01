# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:33:45 2019

@author: willi
"""
import sys

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '' #put your access token
ACCESS_SECRET = '' #put the access secret
CONSUMER_KEY = '' #put the consumer key
CONSUMER_SECRET = '' #put the consumer secret

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# ---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
# ---------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends. 
# This is the equivalent of /timeline/home on the Web.
# The following loop save the mose recent statues of my profile
# ---------------------------------------------------------------------------------------------------------------------
# with open('data.json', 'w') as outfile:
#     for status in tweepy.Cursor(api.home_timeline).items(200):
#         #       print(status._json)
#         res = status._json
#         print(type(res))
#         print(res["coordinates"]!=None)
#         print(res["place"]!=None)
#
#         json.dump(res, outfile)
#         outfile.write("\n")
#
#
#






# ---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
# ---------------------------------------------------------------------------------------------------------------------


class StreamListener(tweepy.StreamListener):
    """
    class to use the Streaming API
    """


    def on_status(self, status):
        print("coordinates : ",status._json["coordinates"])
        print("place: ", status._json["place"])
        print(status._json)
        if status._json["place"]!=None and status._json["place"]["country_code"]=="FR":
            with open('data3.json', 'a', encoding='utf-8') as outfile:
                json.dump(status._json,outfile)
                outfile.write("\n")

                outfile.close()
            with open('data3.json', 'r', encoding='utf-8') as outfile:
                print(len(outfile.readlines()))
                outfile.close()
    def on_error(self, status_code):
        if status_code == 420:
            return False





#
# with open('data2.json','r') as outfile:
#     print(len(outfile.readlines()))
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

france=[-4.67, 42, 8, 51.1485061713]
stream.filter(track=["Sida","VIH","AIDS","Aids","HIV",], languages=["fr"],locations=france)

# with open('data2.json','r') as outfile:
#     print(len(outfile.readlines()))
# # ============================================= Open a json file (Json forms) ===============================================
# # We use the file saved from last step as example
# tweets_filename = 'data2.json'
# tweets_file = open(tweets_filename, "r")
#
# for line in tweets_file:
#     print(len(line))
#     # Read in one line of the file, convert it into a json object
#     print("oker1")
#     tweet = json.loads(line.strip())
#     print("oker")
#     if 'text' in tweet:  # only messages contains 'text' field is a tweet
#         print(tweet['id'])  # This is the tweet's id
#         print(tweet['created_at'])  # when the tweet posted
#         print(tweet['text'])  # content of the tweet
#
#         print(tweet['user']['id'])  # id of the user who posted the tweet
#
#         print(tweet['user']['name'])  # name of the user, e.g. "Wei Xu"
#         print(tweet['user']['screen_name'])  # name of the user account, e.g. "cocoweixu"
#         # to catch the location, the key is in location and there is the noun the the city
#         # or there are some GPS coordinates in the dictionary "bounding box"
#
#         hashtags = []
#         for hashtag in tweet['entities']['hashtags']:
#             hashtags.append(hashtag['text'])
#         print(hashtags)

# ================== 3 kinds of API for Twitter : Search (tweets contain certain words), Trends (trending topics) and user (user's tweet, followers, friend...)
###================ SEARCH API 

# # Search for latest tweets about "#nlproc"
# tweets = tweepy.Cursor(api.search, q=['sida','vih','VIH','prevention'])
# # print(json.dumps(tweets))
#
# with open('data2.json', 'w', encoding='utf-8') as outfile:
#     for status in tweets.items(500):
#         print(status.text)
#         print(status.retweeted)
#         res = status._json
#
#         json.dump(res, outfile)
#         outfile.write("\n")
# #
#

# for status in tweets:
#    print(status._json)
### Search for 10 most recent tweets about "#nlproc"
# tweets = tweepy.Cursor(api.search, q='#nlproc', count=10)
#
## Search for latest tweets written in english about "#nlproc"
# tweets = tweepy.Cursor(api.search, q='#nlproc', lang='en')
#
