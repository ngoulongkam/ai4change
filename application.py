from flask import Flask
from flask import jsonify
import tweepy
import auth
from monkeylearn import MonkeyLearn
import monkeylearn_credentials

application = Flask(__name__)


@application.route("/latest", methods=["GET"])
def get_latest_messages():
    api = tweepy.API(auth.auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        ml = MonkeyLearn(monkeylearn_credentials.MONKEY_AUTH_TOKEN)
        data = [tweet.text]
        model_id = 'cl_pi3C7JiL'
        result = ml.classifiers.classify(model_id, data)
        return jsonify(result.body), 200


if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0', port=1337, threaded=True)
