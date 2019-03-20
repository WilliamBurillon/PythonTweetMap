# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:26:43 2019

@author: Corentin BALLAZ
"""


try:
    import json
except ImportError:
    import simplejson as json
    
import mysql.connector

mydb = mysql.connector.connect(host="localhost",
user="root",
passwd="",
database="tweepy")
mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS Tweets (
      id varchar(20) NOT NULL,
      nom varchar(100) DEFAULT NULL,
      text varchar(200) DEFAULT NULL,
      creation_date varchar(100) DEFAULT NULL,
      PRIMARY KEY(id)
      )""")


tweets_filename = 'data2.json'
tweets_file = open(tweets_filename, "r")


for line in tweets_file:
    dic = {}
    # Read in one line of the file, convert it into a json object
    tweet = json.loads(line.strip())

    dic["id"]=tweet["id_str"]
    dic["creation_date"]=tweet["created_at"]
    dic["text"]=tweet["text"]
    dic["name"] = tweet['user']['name']
    
    if 'text' in tweet:  # only messages contains 'text' field is a tweet
        try:
            mycursor.execute("""INSERT INTO Tweets (id, nom, text, creation_date) VALUES(%(id)s ,%(name)s ,%(text)s ,%(creation_date)s)""", dic)
            mydb.commit()
        except:
            try:
                mycursor.execute("""UPDATE Tweets SET nom=%(name)s WHERE id=%(id)s""", dic)
                print("exception : alrealdy in data_base")
            except:
                mycursor.execute("""UPDATE Tweets SET nom=null WHERE id=%(id)s""", dic)
                continue
           
          


            # print(tweet['created_at'])  # when the tweet posted
            # print(tweet['text'])  # content of the tweet
            #
            # print(tweet['user']['id'])  # id of the user who posted the tweet
            # print(tweet['user']['name'])  # name of the user, e.g. "Wei Xu"
            # print(tweet['user']['screen_name'])  # name of the user account, e.g. "cocoweixu"
            #
            # hashtags = []
            # for hashtag in tweet['entities']['hashtags']:
            #     hashtags.append(hashtag['text'])
            # print(hashtags)
            # print('\n')





