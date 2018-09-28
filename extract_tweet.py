from flask import Flask
from flask import jsonify
import tweepy
import auth
from monkeylearn import MonkeyLearn
import monkeylearn_credentials
from tweepy.streaming import StreamListener
from tweepy import Stream
import json

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        print(tweet["text"])
        data = [tweet["text"]]

        ml = MonkeyLearn(monkeylearn_credentials.MONKEY_AUTH_TOKEN)
        model_id = 'cl_pi3C7JiL'

        result = ml.classifiers.classify(model_id, data)

        print(result.body)

        # tweets_data.append(tweet)
    except:
        continue


print("Number of tweet in file: " + str(len(tweets_data)))


# tweets = pd.DataFrame()
# tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
# tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] is not None else None, tweets_data)
# print(tweets)
