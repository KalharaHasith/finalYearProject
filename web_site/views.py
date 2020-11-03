from django.http import HttpResponse
from django.shortcuts import render
# from .sentimentWEB import calculateRating
import pickled as s
import tweepy
import math

api_key = 'cmXgPsjaKK9qRIkFUJZWIGQgw'
api_Key_secret = 'OHIDledtMyWJKdKDlwhQFyGJ06aNpmI2orkavVwcV82uKwdiRz'
access_token = '3491258594-4VoK2YkVOdEuVh3JIOOQSIlbhkC3NuHSbAQov9Y'
access_token_secret = 'O6WFVitUBuDAsoNrA0DMbAWJdIH9jBDekktl9CYtRXps3'

auth_handler = tweepy.OAuthHandler(api_key, api_Key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)


def home(request):
    return render(request, 'home.html')


def count(request):
    # rated_value = calculateRating()
    tweet_amount = 200
    movie_name = request.GET['movie_name']
    # List_tweets = []
    tweets = tweepy.Cursor(api.search, q=movie_name, lang='en').items(tweet_amount)

    list_tweet = []
    polarity = 0
    positive_tweet = 0
    negative_tweet = 0
    # print(movie_name)

    for tweet in tweets:
        tweet_text = tweet.text
        if 'RT @' not in tweet_text:  # to avoid retweet content(duplicate tweets0
            if tweet_text.startswith('@'):  # remove twitter handle
                position = tweet_text.index('')
                tweet_text = tweet_text[position + 2:]
            list_tweet.append(tweet_text)
            # print(tweet_text)

    for processed_tweet in list_tweet:
        search_sentiment = s.sentiment(processed_tweet)
        # print(f'{processed_tweet}   : your confidence = {search_sentiment}')

        if search_sentiment[0] == 'pos' and search_sentiment[1] >= 0.8:
            positive_tweet += 1
        elif search_sentiment[0] == 'neg' and search_sentiment[1] >= 0.8:
            negative_tweet += 1
            neg = math.floor(negative_tweet / 20)  # because negative tweet count is too high

    print(f'Number of positive tweets: {positive_tweet}')
    print(f'Number of negative tweets: {negative_tweet}')

    rating = round((positive_tweet / (positive_tweet + neg)) * 10, 2)  # round the value to two decimal points
    print(f'Rating for your movie is {rating}')

    return render(request, 'count.html', {'movieName': movie_name, 'rating': rating })


def about(request):
    return render(request, 'about.html')