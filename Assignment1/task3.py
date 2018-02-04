#!/usr/bin/python
'''
Author:		Maggie Thomann
File:		task3.py
Date:		Monday Feb 5, 2018
Description:	Collecting tweets in real-time filtered by specified keywords and geo-location
'''
# Libary Imports
import tweepy

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
keywordfile = open('keywordtweets.txt','w')
geofile = open('geofile.txt','w')

# Create the stream
listener = StdOutListener()
stream = Stream(auth, listener)

# Filter the stream
stream.filter(track=keywords)
