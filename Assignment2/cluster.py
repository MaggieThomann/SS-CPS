#!/usr/bin/python
'''
Author:		Maggie Thomann
File:		cluster.py
Date:		Monday Feb 19, 2018
Description:	Implements k-means clustering using the Jaccard distance 
		for a set of tweets
'''

# distance:	Computes the Jaccard distance between a pair of tweets

# cluster:	Clusters the tweets into groups according to their jaccard distance
#		and centroids
def cluster(k, tweets, seeds):
	print "k is "+str(k)



# read_file:	Reads in the file of tweets and returns it as a list
def read_file(file):
	f = open(file)
	tweets = []
	for line in f:
		tweets.append(line)
	return tweets

# read_seeds:	Reads in the initial seeds from the file and returns it as a list
def read_seeds(file):
	f = open(file)
	seeds = []
	for line in f:
		seed = line[:-1]
		seeds.append(seed)
	return seeds



# Main Execution
tweets = read_file('tweets.json')
seeds = read_seeds('initial_seeds.txt')
cluster(25, tweets, seeds)


