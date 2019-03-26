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


class TweepyInDB:
    
    def __init__(self,tweets_filename):
       self.tweets_filename = tweets_filename
       self.initDB()
       
    def __str__(self):
        return self.tweets_filename


    def initDB(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="tweepy")
        self.mycursor = self.mydb.cursor()
        
    
    def createTable(self):
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Tweets (
                id varchar(20) NOT NULL,
                nom varchar(100) DEFAULT NULL,
                text varchar(300) DEFAULT NULL,
                quoted_status_text varchar(300) DEFAULT NULL,
                creation_date varchar(100) DEFAULT NULL,
                position_X varchar(20) DEFAULT NULL,
                position_Y varchar(20) DEFAULT NULL,
                PRIMARY KEY(id)
                )""")
        self.mydb.commit()

    def deleteTable(self):
        try:
            self.mycursor.execute("""DROP TABLE Tweets""")
        except:
            print("error : table doesn't exists")
        
    def viderTable(self):
        try:
            self.mycursor.execute("""TRUNCATE TABLE Tweets""")
        except:
            print("error : table is already empty")
        
        
    def insertIntoTable(self):
        tweets_file = open(self.tweets_filename, "r") 
        for line in tweets_file:
            dic = {}
            # Read in one line of the file, convert it into a json object
            tweet = json.loads(line.strip())
        
            dic["id"]=tweet["id_str"]
            dic["creation_date"]=tweet["created_at"]
            dic["text"] = ''
            dic["name"] = ''
            
            try :
                dic["position_X"] = str((tweet["place"]["bounding_box"]["coordinates"][0][0][1] + tweet["place"]["bounding_box"]["coordinates"][0][1][1])/2.0)
                dic["position_Y"] = str((tweet["place"]["bounding_box"]["coordinates"][0][0][0] + tweet["place"]["bounding_box"]["coordinates"][0][2][0])/2.0)
            except :
                print("error : localisation doesn't exists")
                continue

            
            for i in range(0,len(tweet["text"])):
                if (tweet["text"][i] <= 'ü'):
                    dic["text"]= dic["text"] + tweet["text"][i]
            for j in range(0,len(tweet["user"]["name"])):
                if (tweet["user"]["name"][j] <= 'ü'):
                    dic["name"] = dic["name"] + tweet['user']['name'][j]
                    
            try:
                dic["quoted_status_text"] = ''
                for k in range(0,len(tweet["quoted_status"]["text"])):
                    if (tweet["quoted_status"]["text"][k] <= 'ü'):
                        dic["quoted_status_text"]= dic["quoted_status_text"] + tweet["quoted_status"]["text"][k]
            except:
                dic["quoted_status_text"] = None
            #deux boucles pour régler le problème des émoticones
        
            
            if 'text' in tweet:  # only messages contains 'text' field is a tweet
                try:
                    self.mycursor.execute("""INSERT INTO Tweets (id, nom, text, quoted_status_text, creation_date, position_X, position_Y) VALUES(%(id)s ,%(name)s ,%(text)s ,%(quoted_status_text)s ,%(creation_date)s ,%(position_X)s ,%(position_Y)s)""", dic)
                    self.mydb.commit()
                except:
                    #print("error : line already in database")
                    continue          




objet = TweepyInDB('data3.json')
#objet.deleteTable()
#objet.createTable()
#objet.insertIntoTable()
#objet.viderTable()



