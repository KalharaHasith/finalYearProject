import tweepy
import pickled as s
import sys
import math

api_key = 'cmXgPsjaKK9qRIkFUJZWIGQgw'
api_Key_secret = 'OHIDledtMyWJKdKDlwhQFyGJ06aNpmI2orkavVwcV82uKwdiRz'
access_token = '3491258594-4VoK2YkVOdEuVh3JIOOQSIlbhkC3NuHSbAQov9Y'
access_token_secret = 'O6WFVitUBuDAsoNrA0DMbAWJdIH9jBDekktl9CYtRXps3'

auth_handler = tweepy.OAuthHandler(api_key, api_Key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'The Croods'
tweet_amount = 200

List_tweets = []
tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)

list_tweet = []
polarity = 0
positive_tweet = 0
negative_tweet = 0

# for tweet in tweets:
#     cleared_rt = tweet.text.replace('RT', '')
#     if cleared_rt.startswith(' @'):
#         position = cleared_rt.index(':')
#         cleared_rt = cleared_rt[position+2:]
#     if cleared_rt.startswith('@'):
#         position = cleared_rt.index('')
#         cleared_rt = cleared_rt[position+2:]
#     list_tweet.append(cleared_rt)
#     # print(tweet.text)
# # print(list_tweet)
#
# for rt in list_tweet:
#     ef = s.sentiment(rt)
#     print(f'{rt}   : your confidence = {ef}')
#
#     if ef[0] == 'pos':
#         positive_tweet += 1
#     elif ef[0] == 'neg':
#         negative_tweet += 1
#
# print(positive_tweet)
# print(negative_tweet)
#
# rating = (positive_tweet/tweet_amount) * 10
# print(f'Rating for your movie is {rating}')

'''
Need to remove youtube links from tweets ;)
'''

for tweet in tweets:
    tweet_text = tweet.text
    if 'RT @' not in tweet_text:   # to avoid retweet content(duplicate tweets0
        if tweet_text.startswith('@'):   # remove twitter handle
            position = tweet_text.index('')
            tweet_text = tweet_text[position+2:]
        list_tweet.append(tweet_text)
        # print(tweet_text)

for processed_tweet in list_tweet:
    search_sentiment = s.sentiment(processed_tweet)
    print(f'{processed_tweet}   : your confidence = {search_sentiment}')

    if search_sentiment[0] == 'pos' and search_sentiment[1] >= 0.8:
        positive_tweet += 1
    elif search_sentiment[0] == 'neg' and search_sentiment[1] >= 0.8:
        negative_tweet += 1
        neg = math.floor(negative_tweet/20)  # because negative tweet count is too high

print(f'Number of positive tweets: {positive_tweet}')
print(f'Number of negative tweets: {negative_tweet}')

rating = round((positive_tweet/(positive_tweet + neg)) * 10, 2)  # round the value to two decimal points
print(f'Rating for your movie is {rating}')
