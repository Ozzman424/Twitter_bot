# Twitter_bot
A bot that sends news updates from popular stock trading creators

#Explanation

1. fetch_tweets.py:

* Authenticates with the Twitter API using Tweepy.
* Fetches recent tweets from specified Twitter handles.
* Saves the tweets to a JSON file.

2. ProcessTweets.java:

* Reads the JSON file containing fetched tweets.
* Sends an email notification for each tweet using JavaMail API.
