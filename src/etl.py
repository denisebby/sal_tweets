
import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

import os
from dotenv import load_dotenv

def run_twitter_etl():

    load_dotenv()

    bearer_token = os.getenv("BEARER_TOKEN")

    # work with Twitter v2 API
    client = tweepy.Client(bearer_token=bearer_token)

    username = "SalVulcano"
    account = client.get_user(username=username)
    tweets = client.get_users_tweets(id = account.data.id,  max_results = 100, exclude = "retweets,replies")

    list1 = []
    for tweet in tweets[0]:

        refined_tweet = {"user": username,
                        "tweet_id": tweet.id,
                        'text' : tweet.text,
                        }
        
        list1.append(refined_tweet)

    df = pd.DataFrame(list1)

    #  save locally
    # df.to_csv('refined_tweets.csv', index = False)

    df.to_csv('s3://sal_tweets/refined_tweets.csv', index = False)

if __name__=="__main__":
    run_twitter_etl()