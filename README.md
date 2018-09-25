AI4Change
===================
### About

Created for the Capgemini AI 4 Change hackathon challenge, this is a simple tool to analyse the sentiment of tweets. Developed for learning purposes.

### Service Definitions

The port for this service is 1337

### Run the application locally
```bash
FLASK_APP=application.py flask run --port=1337
```

### Setup Information
Further information on machine and authentication credential setup can be found below.

| *Task* | *Description* | *Documentation* |
|--------|----|----|
| Machine Setup | Instructions for setting up python and virtualenv on your local machine | [Machine Setup](docs/machine_setup.md) |
| Twitter Developer Account Setup | Instructions for setting up a Twitter Developer Account and add a credentials file to the project | [Twitter Developer Account Setup](docs/twitter_account_setup.md) |
| MonkeyLearn Account Setup | Instructions for creating a MonkeyLearn account and obtaining your API_KEY | [MonkeyLearn Account Setup](docs/monkeylearn_setup.md) |

### API

| *Task* | *Supported Methods* | *Description* |
|--------|----|----|
| ```/latest``` | GET | Retrieves the latest tweet from your own timeline and runs it through sentiment analysis. |

### Additional Options

There are 2 additional scripts available.

| *Name* | *Description* |
|--------|----|
| hello_tweepy.py | Grabs some of the latest tweets from your home timeline. |
| twitter_stream.py | Listens for any new, live tweets with specific keywords. |

To execute a python script, simply write `python` [filename].py 
```
python hello_tweepy.py
```