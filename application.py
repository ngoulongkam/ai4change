from flask import Flask
from flask import jsonify
import tweepy
import auth
from monkeylearn import MonkeyLearn
import monkeylearn_credentials
import json

application = Flask(__name__)
ml = MonkeyLearn(monkeylearn_credentials.MONKEY_AUTH_TOKEN)
model_id = 'cl_pi3C7JiL'


@application.route("/latest", methods=["GET"])
def get_latest_messages():
    api = tweepy.API(auth.auth)

    public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     data = [tweet.text]
    #     result = ml.classifiers.classify(model_id, data)
    #     # Data needed
    #     # sentimentData[] - created_at (tweet), confidence(ml), tag_name(ml), text(tweet,ml)
    #     # confidenceLevel - averagePositiveConfidence(calc)
    #     # averageNeutralConfidence(calc), averageNegativeConfidence(calc), time_zone(tweet)
    response = build_response(public_tweets)
    return jsonify(response), 200


def build_response(public_tweets):
    sentiment_data = {}
    for tweet in public_tweets:
        data = [tweet.text]
        ml_result = json.loads(ml.classifiers.classify(model_id, data))
        sentiment_data.update({"created_at": tweet.created_at})
        sentiment_data.update({"confidence": ml_result.body['classifications']['confidence']})
        sentiment_data.update({"tag_name": ml_result.body['classifications']['tag_name']})
        sentiment_data.update({"text": tweet.text})
    return jsonify(sentiment_data)


if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=1337, threaded=True)
