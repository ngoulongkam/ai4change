Twitter Account Setup
===================

## Set up Twitter account and apply as developer 

1. Create an account on Twitter

2. Apply as a developer on: https://apps.twitter.com/

3. Once applied as a developer, create an app

## Generate Keys and Tokens

Once an app has been created, you can navigate to 'Keys and tokens' to generate the `API key`, `API secret key`, `Access token` and `Access token secret`

Clone this repo and create a new file called: `twitter_credentials.py` 

Inside the `twitter_credentials.py` file, write the following:

```
ACCESS_TOKEN = "xxxxxxxxx"
ACCESS_TOKEN_SECRET = "xxxxxxxxx"
CONSUMER_KEY = "xxxxxxxxx"
CONSUMER_SECRET = "xxxxxxxxx"
```
Where `xxxxxxxxx` are the keys generated in the step above, ensure you copy the correct key into the correct variable otherwise you won't be able to execute the script.