import tweepy
import pickled as s
import sys

api_key = 'cmXgPsjaKK9qRIkFUJZWIGQgw'
api_Key_secret = 'OHIDledtMyWJKdKDlwhQFyGJ06aNpmI2orkavVwcV82uKwdiRz'
access_token = '3491258594-4VoK2YkVOdEuVh3JIOOQSIlbhkC3NuHSbAQov9Y'
access_token_secret = 'O6WFVitUBuDAsoNrA0DMbAWJdIH9jBDekktl9CYtRXps3'

auth_handler = tweepy.OAuthHandler(api_key, api_Key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = 'Wonder Women'
tweet_amount = 200






