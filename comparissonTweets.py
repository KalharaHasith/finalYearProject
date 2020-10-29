import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List

import pickled as s

ckey = "BNPj5RN5YFrBkoy8FCSSUADXc"
csecret = "zeuNOocezOH1wRWujUBINT4CvKumEtpJW0ql2CQx1SqpNfwj6E"
atoken = "2902474477-UxJR8N06sjNIXuaGlGk0IPsPtb2UYoWnhq3D4YL"
asecret = "TPti3ngvexZCcnzN27jPlx6fz7wc5f24aHJDoddJIf2KE"

auth = tweepy.AppAuthHandler(ckey, csecret,)
api = tweepy.API(auth)


def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(10):
        all_tweets.append(tweet.full_text)

    return all_tweets


def clean_tweets(all_tweets: str) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean


def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
        # sentiment_scores.append(s.sentiment(tweet))
    return sentiment_scores


def generate_avg_sentiment_score(keyword: str) -> int:
     tweets = get_tweets(keyword)
     tweets_clean = clean_tweets(tweets)
     sentiment_scores = get_sentiment(tweets_clean)
     average_score = statistics.mean(sentiment_scores)

     return average_score


if __name__ == "__main__" :
    print('what does the world prefers')
    first_name = input()
    print('----or---')
    second_name = input()
    print('\n')

    first_score = generate_avg_sentiment_score(first_name)
    second_score = generate_avg_sentiment_score(second_name)

    if first_score > second_score :
        print(f'world prefer {first_name} over {second_name}')
    else:
        print(f'world prefer {second_name} over {first_name}')

