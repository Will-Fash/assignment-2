#!/usr/bin/env python3
import tweepy
import csv

consumer_key = 'fcICOiKLBLxbGwa3QBRFsLhTH'
consumer_secret = 'l1CxBSyJ7KBOaKjsuALAqAPJIQKKnVQ9UHc2QxQ3Il1H0NrNau'
access_token = '1000390707436285952-RMrJcW3RaDDnuxtChOhiGX6QXypPWG'
access_token_secret = '8spBEkKpmcR9G2wVNpPns5W59xm9JevLi1GIvOOIBBeVu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
with open ('tweets.csv', 'w') as outfile:
    csvWriter = csv.writer(outfile)
    for tweet in tweepy.Cursor(api.search,q="#realDonaldTrump",count=100,
    lang="en",
    since="2018-05-20").items(100):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])