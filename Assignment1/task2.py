#!/usr/bin/python
'''
Author:		Maggie Thomann
File:		task2.py
Date:		Monday Feb 5, 2018
Description:	Twitter crawler of user friends+followers information
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
f = open('task2output.txt','w')

# Keep a list of retrieved users
users_list = []

# Store what to write to output
output_list = 	["The Friends List:", "The Followers List:"]

# Loop through ids and get info
for id in user_ids:
	user_obj = []
	user = api.get_user(id)
	followers = user.followers()
	friends = user.friends()
	friends_list = []
	followers_list = []	
	for follower in followers:
		followers_list.append(follower.screen_name)
	for friend in friends:
		friends_list.append(friend.screen_name)
	users_list.append(friends_list)
	users_list.append(followers_list)

# Write to the file
index = 0
for user in user_ids:					# Loop through the users to retrieve
	print "Writing to file for user: "+str(user)	
	for output in output_list:			# Loop through the two outputs
		f.write(output+"\n\n")
		for name in users_list[index]:		# Loop through all names for each output
			f.write(name+"\n")
		index += 1
		f.write("\n\n")
	f.write("\n")

f.close()


