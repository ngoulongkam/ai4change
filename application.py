from flask import Flask
from flask import jsonify
import tweepy
import auth
from monkeylearn import MonkeyLearn
import monkeylearn_credentials
from tweepy.streaming import StreamListener
from tweepy import Stream
import json

application = Flask(__name__)

tweets_data_path = 'twitter_data.txt'


@application.route("/latest", methods=["GET"])
def get_latest_messages():

    tweets_data = []
    with open(tweets_data_path, "r") as f:
        for line in f:
            try:
                # load file
                tweet = json.loads(line)
                # extract "text" field from file
                data = [tweet["text"]]
                # ML cred
                ml = MonkeyLearn(monkeylearn_credentials.MONKEY_AUTH_TOKEN)
                model_id = 'cl_pi3C7JiL'

                result = ml.classifiers.classify(model_id, data)
                # print(tweet["text"])
                tweets_data.append(result.body)
                print(tweets_data)
                return jsonify(tweets_data), 200
            except:
                continue


    # api = tweepy.API(auth.auth)

    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     ml = MonkeyLearn(monkeylearn_credentials.MONKEY_AUTH_TOKEN)
    #     data = [tweet.text]
    #     model_id = 'cl_pi3C7JiL'
    #     result = ml.classifiers.classify(model_id, data)
    #     return jsonify(result.body), 200


class StdOutListener(StreamListener):

    def on_data(self, data):
        f = open('twitter_data.txt', 'a')
        f.write(data)
        return True

    def on_error(self, status):
        print(status)


@application.route("/stream-tweet", methods=["GET"])
def streamTweet():
    listener = StdOutListener()
    oauth = auth.auth
    auth.authAccessToken

    stream = Stream(oauth, listener)
    stream.filter(track=['capgemini', 'Capgemini', 'sogeti'])


if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=1337, threaded=True)
