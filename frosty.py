import tweepy
import os
import pickle
import inflect
import sys
from random import choice, random
import unicodedata
from credentials import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
)


# SETUP
# Twitter API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Setup inflect engine
p = inflect.engine()

# Probability that determines when the zalgo process starts
zalgo_trigger_probability = 0.05

# Tweet character limit
CHAR_LIMIT = 250

# LOAD COUNTS
# Path to pickle file which will store the times tweeted to disk
times_tweeted_path = './times_tweeted.p'

# Path to pickle file which will store the zalgo number.
# I could have put this in the times tweeted pickle, but
# I think this is cleaner / backwards compatible.
zalgo_number_path = './zalgo_number.p'

# Load count stored from disk if it exists
if os.path.isfile(times_tweeted_path):
    with open(times_tweeted_path, 'rb') as f:
        times_tweeted = pickle.load(f)
else:
    times_tweeted = 0

# Load zalgo number from disk if it exists
if os.path.isfile(zalgo_number_path):
    with open(zalgo_number_path, 'rb') as f:
        zalgo_number = pickle.load(f)
else:
    zalgo_number = -1  # zalgo not triggered


# CONSTRUCT BASE TWEET
# Construct the pre-proclamation count phrase.
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
tweet = pre_proclamation + proclamation


# ZALGO TIME
# If zalgo hasn't been triggered, apply trigger with trigger probability.
if zalgo_number == -1:
    if random() <= zalgo_trigger_probability:
        zalgo_number = 1  # start at zalgo number 1
# Apply zalgo to tweet string.
else:
    # number of zalgo marks added to each character
    num_marks = int(zalgo_number ** 2 / 2)  # grows exponentially
    marks = list(map(chr, range(768, 879)))  # combining diacritical marks
    words = tweet.split()

    # Randomly add marks to alphanumeric characters in each word, and join.
    # The probability that a char gets marks increases with the zalgo number.
    tweet = ' '.join(''.join(
        c + ''.join(choice(marks) for _ in range(num_marks)
                    if (random() * 100) < zalgo_number) * c.isalnum()
        for c in word)
        for word in words)

    # reduce tweet length by normalizing
    tweet = unicodedata.normalize('NFC', tweet)  # Unicode Normalization Form C

    # break tweet into multiple tweets to adhere to twitter char limit
    # (twitter counts chars a little more intelligently, but this will do)
    tweets = [tweet[i:i + CHAR_LIMIT] for i in range(0, len(tweet), CHAR_LIMIT)]


# TWEET
# Attempt to update status- print error and exit on failure
prev_status = None
try:
    for tweet in tweets:
        if prev_status is None:
            prev_status = api.update_status(tweet)
        else:  # reply to previous status
            prev_status = api.update_status(
                tweet,
                in_reply_to_status_id=prev_status.id)
except Exception as e:
    print('Twitter Status Update Error: {}'.format(e))
    sys.exit(1)


# UPDATE
# Update counters on disk if the tweet was successfully posted
times_tweeted += 1
if zalgo_number != -1:
    zalgo_number += 1
print('Successfully tweeted, tweet number {}, zalgo number {}'.format(
    times_tweeted, zalgo_number))
with open(times_tweeted_path, 'wb') as f:
    pickle.dump(times_tweeted, f)
with open(zalgo_number_path, 'wb') as f:
    pickle.dump(zalgo_number, f)
