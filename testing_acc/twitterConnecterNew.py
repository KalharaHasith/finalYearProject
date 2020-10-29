import tweepy
from tweepy import OAuthHandler
# from . import dbConnector
import pickled as s


''' testing purpose only
'''


class twitterConnector(object):
    ckey = 'BNPj5RN5YFrBkoy8FCSSUADXc'
    csecret = 'zeuNOocezOH1wRWujUBINT4CvKumEtpJW0ql2CQx1SqpNfwj6E'
    atoken = '2902474477-UxJR8N06sjNIXuaGlGk0IPsPtb2UYoWnhq3D4YL'
    asecret = 'TPti3ngvexZCcnzN27jPlx6fz7wc5f24aHJDoddJIf2KE'

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)

    def searchTwitter(self, movieName):
        # connectorObj = dbConnector.dbConnector()
        # dbConnector class in dbConnector.py file.

        # connectorObj.deleteAll()

        for tweet in tweepy.Cursor(self.api.search, lang='en', q=movieName).items(200):
            # Tweet objects are returned by Tweepy module. No need to have a seperate Tweet class.
            # To access static variables inside a method, 'self.api'. Can also use 'twitterConnector.api'

            if 'RT @' not in tweet.text:
                # to avoid retweets and thereby duplicates

                # username = tweet.user.name
                # tweetContent = tweet.text
                # publishedDate = tweet.created_at
                #
                # connectorObj.saveTweet(username, tweetContent, publishedDate)
                print(tweet, sentiment_value, confidence)

                if confidence * 100 > 80:
                    output = open('twiter.txt', 'a')
                    output.write(sentiment_value)
                    output.write('\n')
                    output.close()

                return True

    def numberOfTweets(self):
        connectorObj = dbConnector.dbConnector()
        return connectorObj.retrieveTweets().count()
