#!/usr/bin/python
'''
Author:		Maggie Thomann
File:		task3.py
Date:		Monday Feb 5, 2018
Description:	Collecting tweets in real-time filtered by specified keywords and geo-location
'''
# Libary Imports
import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener

# Class for listener
class Listener(StreamListener):
	def __init__(self, type):
		self.keywordtweets = []
		self.geolocationtweets = []
		self.type = type

	def on_data(self, data):
		
		all_data = json.loads(data)
		tweet = all_data["text"]
		if self.type == "keywords":
		 	self.keywordtweets.append(tweet)
			if len(self.keywordtweets) == 50:
				return False
			else:
				return True 
		elif self.type == "geolocation":
		 	self.geolocationtweets.append(tweet)
			if len(self.geolocationtweets) == 50:
				return False
			else:
				return True 


	def on_error(self, status):
		 print status

# Keys for API Access
consumer_key = "cnHTXNSLFTkFlCK8yXKpfA4hP"
consumer_secret = "Ildp8Op7R7uBhwyL8ZqpWLHjWrtfe5PQpKsVd5kJ92CrXf6aQI"
access_token = "748519320024657920-PCmjAjMqSfIJikWICcqBH45xpNy29DJ"
access_token_secret = "M3N1UUNS8qY10WCyHWuEbygsWplmB3VAaxSKjboII09fd"

# Handling Oauth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Keywords for assignment
keywords = ["Indiana", "weather"]

# Geo location for assignment
geolocation = [-86.33,41.63,-86.20,41.74]

# Create output file
keywordfile = open('task3output-keywordtweets.txt','w')
geofile = open('task3output-geofile.txt','w')

# Create the listener
listener = Listener("keywords")
geolistener = Listener("geolocation")

# Create the keyword stream
stream = Stream(auth, listener)

# Create the geo stream
geostream = Stream(auth, geolistener)

# Filter the stream
stream.filter(track=keywords, languages=["en"])
geostream.filter(locations=geolocation, languages=["en"])

# Add it to the file
count = 1
for tweet in listener.keywordtweets:
	keywordfile.write(str(count) + ":  "+tweet.encode('utf-8')+"\n"+"\n")
	count += 1

count = 1
for tweet in geolistener.geolocationtweets:
	geofile.write(str(count) + ":  "+tweet.encode('utf-8')+"\n"+"\n")
	count += 1

# Close the file
keywordfile.close()
geofile.close()




