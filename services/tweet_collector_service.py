from TweetCollector import TweetCollector
import json

agencies_file = './data/resources/agencies.json'

agencies = {}
with open(agencies_file) as f:
    agencies = json.load(f)

# for agency in agencies:
#     print(agencies[agency]['handle'])

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

print('Starting the tweet collector:\n')
tc = TweetCollector(agencies, access_token, access_token_secret, consumer_key, consumer_secret)
input('')
