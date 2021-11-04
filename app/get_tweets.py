import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "HUFlzhnxJbLOqIYaWhXo6VZaz"
# api secret key
api_secret_key = "KfiPKZkOpMdI5ony1UXSIYWsICLj9TOkmyQUHqRI488Vs6QWiJ"
# access token
access_token = "1389549456916369408-RnjzLjZZ8YCJo61KA0zOMLT46RZFJq"
# access token secret
access_token_secret = "HrA0iQsn10eotYmwu5E5iIuXutAH1dOlc67tS3M1OPYES"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
        
get_related_tweets("violence")