#!/usr/bin/python
'''
Author:		Maggie Thomann
File:		cluster.py
Date:		Monday Feb 19, 2018
Description:	Implements k-means clustering using the Jaccard distance 
		for a set of tweets
Usage:		Python cluster.py
'''
import json

# distance:			Computes the Jaccard distance between a pair of tweets
def distance(a, b):
	intersection = list(set(a) & set(b))
	intersection_length =len(intersection)
	union = list(set(a) | set(b))
	union_length = len(union)
	distance = 1 - (float(intersection_length)/union_length)
	return distance

# compute_new_centroids:	Computes new centroids based on how the data points
#				were assigned to the clusters.
def compute_new_centroids(tweets, mean_indices):
	if len(mean_indices) > 0:
		# Construct the text from the indices
		mean_tweets = []
		for index in mean_indices:
			mean_tweets.append(tweets[index]['text'].lower().split())

		# Get the distances
		distances = []
		for i in range(len(mean_indices)):
			inner_distances = []
			for j in range(len(mean_indices)):
				dist = distance(mean_tweets[i], mean_tweets[j])
				inner_distances.append(dist)
			distances.append(inner_distances)
		# Sum all the distances
		sums = []
		for inner_distance in distances:
			sum_dist = sum(inner_distance)
			sums.append(sum_dist)
	return [distances, sums]


# cluster:			Clusters the tweets into groups according to their jaccard distance
#				and centroids
def cluster(k, tweets, ids, seeds):
	print "Performing clustering..."
	# Perform the clustering
	for i in range(len(seeds)):

		# Get the tweets for each centroid
		centroid_tweets = []
		for tweet in tweets:
			id = tweet['id']
			for seed in seeds:
				if str(id) == str(seed):
					# Make the tweet a list of words
					list_tweet = tweet['text'].lower().split()
					centroid_tweets.append(list_tweet)

		# Create each cluster
		cluster = []
		for tweet in tweets:
			distances = []
			for j in range(k):
				dist = distance(tweet['text'].lower().split(), centroid_tweets[j])
				distances.append(dist)
			minimum_distance  = min(distances)
			index_of_minimum_distance = distances.index(minimum_distance)
 			cluster.append(index_of_minimum_distance)

 			

 		indices = []
 		new_centroid_indices = []
 		for kmean in range(k):
 			indices_list = []
			for tweet_id, cluster_id in enumerate(cluster):
				if cluster_id == kmean:
					indices_list.append(tweet_id)
			indices.append(indices_list)
			mean_indices=indices[kmean]
			# Compute the new centroids based on the updated assignment of data points to clusters.
 			new_centroid_dist_and_sum = compute_new_centroids(tweets, mean_indices)
 	
		 	dists_sum = []
		 	for dist in new_centroid_dist_and_sum[0]:
		 		sum_dist = sum(dist)
		 		dists_sum.append(sum_dist)
		 	minimum_sum_dist = min(dists_sum)
		 	minimum_sum_dist_index = new_centroid_dist_and_sum[1].index(minimum_sum_dist)
		 	new_centroid_indices.append(mean_indices[minimum_sum_dist_index])

		new_centroids = []
		for index in new_centroid_indices:
			new_centroids.append(ids[index])

		# Compare new and old centroids
		total_sum = 0
		for index in range(k):
			if (new_centroids[index]==seeds[index]):
				total_sum += 1
		if (total_sum == k):		# The algorithm is considered to converge when the assignment of data points to clusters no longer changes.
			break;   
		counter = 0
		for centroid in new_centroids:
			seeds[counter] = centroid
			counter += 1
	# End clustering loop

	# Output to the file
	final_clusters = []
	write_to_file = []
	f = open("results.txt", "w")	
	for mean in range(k):
		list_tweet = []
		for tweet_id, cluster_id in enumerate(cluster):
			if cluster_id == mean:
				list_tweet.append(tweet_id)
		final_clusters.append(list_tweet)
	counter = 1
	for cluster in final_clusters:
		id_list = []
		for id in cluster:
			id_list.append(ids[id])
		print >> f, counter, ":", id_list
		counter += 1
	print "Clustering completed:"
	print "\t Tweets were grouped into "+str(k)+" clusters (results in the results.txt file)."



# read_file:			Reads in the file of tweets and returns it as a list of dicts
def read_file(file):
	f = open(file)
	tweets = []
	ids = []
	for line in f:
		tweet = json.loads(line)
		tweets.append(tweet)
		ids.append(tweet['id'])
	return tweets, ids

# read_seeds:			Reads in the initial seeds from the file and returns it as a list
def read_seeds(file):
	f = open(file)
	seeds = []
	for line in f:
		seed = line.replace(',', '')
		seed = seed.replace('\n', '')
		seeds.append(seed)
	return seeds



# Main Execution
tweets, ids = read_file('tweets.json')
seeds = read_seeds('initial_seeds.txt')
cluster(25, tweets, ids, seeds)


