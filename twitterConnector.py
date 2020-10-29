from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
# import MySQLdb
import time
import json

import pickled as s




#consumer key, consumer secret, access token, access secret.
ckey = "BNPj5RN5YFrBkoy8FCSSUADXc"
csecret = "zeuNOocezOH1wRWujUBINT4CvKumEtpJW0ql2CQx1SqpNfwj6E"
atoken = "2902474477-UxJR8N06sjNIXuaGlGk0IPsPtb2UYoWnhq3D4YL"
asecret = "TPti3ngvexZCcnzN27jPlx6fz7wc5f24aHJDoddJIf2KE"


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)

        # username = all_data["user"]["screen_name"]

        # c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
        #     (time.time(), username, tweet))

        # conn.commit()
        if 'RT @' not in tweet:   # avoid  retweets for remove duplicates
            print(tweet, sentiment_value, confidence)

        if confidence*100 > 80 :
            output = open('twiter.txt', 'a')
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["covid"])