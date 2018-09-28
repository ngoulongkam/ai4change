import json
import pandas as pd

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        print(tweet["text"])
        tweets_data.append(tweet)
        print(tweets_data)
    except:
        continue


print("Number of tweet in file: " + str(len(tweets_data)))


# tweets = pd.DataFrame()
# tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
# tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] is not None else None, tweets_data)
# print(tweets)
