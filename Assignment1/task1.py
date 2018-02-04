#!/usr/bin/python
'''
Author:		Maggie Thomann
File:		task1.py
Date:		Monday Feb 5, 2018
Description:	Twitter crawler of user information
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

# List of user ids for assignment
user_ids = [34373370, 26257166, 12579252]

# Create output file
f = open('task1output.txt','w')

# Keep a list of retreieved users
users_list = []

# Store what to write to output
output_list = 	["Screen Name:", "User Name:", "User Location:",
		"User Description:", "The Number of Followers:",
		"The Number of Friends:", "The Number of Statuses:",
		"User URL:"]

# Loop through ids and get info
for id in user_ids:
	user_obj = []
	user = api.get_user(id)
	user_obj.append(user.screen_name)
	user_obj.append(user.name)
	user_obj.append(user.location)
	user_obj.append(user.description)
	user_obj.append(user.followers_count)
	user_obj.append(user.friends_count)
	user_obj.append(user.statuses_count)
	user_obj.append(user.url)
	users_list.append(user_obj)

# Write to the file
index = 0
for user in users_list:
	for output in output_list:
		print output
		print user[index]
		f.write(output+str(user[index])+"\n")
		index += 1
	f.write("\n")
	index = 0

f.close()
