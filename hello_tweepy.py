import tweepy
import auth

api = tweepy.API(auth.auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
