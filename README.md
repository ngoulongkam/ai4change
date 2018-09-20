AI4Change
===================

### Set up on your machine

Install Brew:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install Python:

```
brew install python
```

Install Pip:

```
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
```

Install Tweepy:

```
pip install tweepy
```
If you have trouble installing tweepy regarding 'six' or 'servicemanager', run the following:

```
sudo pip install tweepy --ignore-installed six servicemanager
```

### Set up Twitter account and apply as developer 

1. Create an account on Twitter

2. Apply as a developer on: https://apps.twitter.com/

3. Once applied as a developer, create an app

### Generate Keys and Tokens

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

### Execute the script

To execute a python script, simply write `python` [filename].py 

for e.g.

```
python hello_tweepy.py
```