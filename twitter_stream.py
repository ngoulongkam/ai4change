from tweepy.streaming import StreamListener
from tweepy import Stream
import auth


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    listener = StdOutListener()
    oauth = auth.auth
    auth.authAccessToken

    stream = Stream(oauth, listener)
    stream.filter(track=['capgemini', 'Capgemini', 'sogeti'])
