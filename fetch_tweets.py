import tweepy
import json
from credentials import TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

# Twitter authentication
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET_KEY,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# List of Twitter handles to monitor
twitter_handles = ['stock_handle_1', 'stock_handle_2', 'stock_handle_3']

# Fetch tweets and save them to a JSON file
def fetch_tweets():
    all_tweets = []
    for handle in twitter_handles:
        tweets = api.user_timeline(screen_name=handle, count=5, tweet_mode="extended")
        for tweet in tweets:
            all_tweets.append({
                'user': handle,
                'text': tweet.full_text,
                'created_at': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
    
    with open('fetched_tweets.json', 'w') as file:
        json.dump(all_tweets, file)

if __name__ == "__main__":
    fetch_tweets()
