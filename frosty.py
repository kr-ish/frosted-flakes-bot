import tweepy
import os
import pickle
import inflect
import sys
from credentials import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
)

# Twitter API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Setup inflect engine
p = inflect.engine()

# Path to pickle file which will store the times tweeted to disk
times_tweeted_path = './times_tweeted.p'

# Load count stored to disk if it exists
if os.path.isfile(times_tweeted_path):
    with open(times_tweeted_path, 'rb') as f:
        times_tweeted = pickle.load(f)
else:
    times_tweeted = 0

# Construct the pre-proclamation count phrase
if times_tweeted == 0:
    pre_proclamation = ''
else:
    if times_tweeted == 1:
        numeral_adverb = 'once'
    elif times_tweeted == 2:
        numeral_adverb = 'twice'
    elif times_tweeted == 3:
        numeral_adverb = 'thrice'
    else:
        numeral_adverb = p.number_to_words(times_tweeted) + ' times'
    pre_proclamation = 'I\'ve said it {} and I\'ll say it again, '.format(
        numeral_adverb)

proclamation = 'Frosted Flakes is the greatest cereal of all time'

# Attempt to update status, if it fails prints the errors and exit
try:
    api.update_status(pre_proclamation + proclamation)
except Exception as e:
    print('Twitter Status Update Error: {}'.format(e))
    sys.exit(1)

# Update counter on disk if tweet was succesfully posted
times_tweeted += 1
with open(times_tweeted_path, 'wb') as f:
    pickle.dump(times_tweeted, f)
