""" A simple example of downloading all tweets to a CSV file """
from __future__ import absolute_import, print_function

import re
import csv
import json
import tweepy

# == OAuth Authentication ==

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
with open("keys/twitter_keys.json") as oauth_file:
    oauth_data = json.load(oauth_file)
    consumer_key = oauth_data['consumer_key']
    consumer_secret = oauth_data['consumer_secret']

    # The access tokens can be found on your applications's Details
    # page located at https://dev.twitter.com/apps (located
    # under "Your access token")
    access_token = oauth_data['access_token']
    access_token_secret = oauth_data['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
tweets = []

for page in range(20):
    new_tweets = [status.text.encode("utf-8") for status in api.user_timeline(api.me().screen_name, count=200, page=page, include_rts=True)]
    tweets += new_tweets
    if len(new_tweets) <= 0:
        break
print(len(tweets), "tweets downloaded.")

# Use regex to clean up the tweets
REMOVALS = [
    r'(https?:\/\/)?[\w-]+(\.[\w-]+)+\.?(:\d+)?(\/\S*)?',
    r'@\w{1,15}',
    r'&\w+;',
]

cleaned_tweets = []

for tweet in tweets:
    for pattern in REMOVALS:
        tweet = re.sub(pattern, '', str(tweet))
    print(tweet)
    cleaned_tweets.append(tweet)

cleaned_tweets = [[tweet] for tweet in cleaned_tweets]

# Write the csv
with open('data/%s_tweets.csv' % api.me().screen_name, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(cleaned_tweets)
