#!/usr/bin/env python3
import csv
import re
import paralleldots

api_key = "PqUvjJ4vyPXCjfInJ3K7uDDwdtam1Rb0GBbV2xP8OPQ"

paralleldots.set_api_key(api_key)
paralleldots.get_api_key()

def processTweet2(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet  

filename = 'tweets.csv'

tide = []
text = []
sentiment = []
score = []
data = []

with open(filename,'r', encoding="utf8", errors = 'ignore') as csvfile: 
    reader = csv.reader(csvfile)
    for row in reader:
        tide.append(row[1])

for line in tide:
    text.append(processTweet2(line))
#print(will)



for w in range(len(text)):
    json_data = paralleldots.sentiment(text[w])
    for k,v in json_data.items():
        if k == 'sentiment':
            sentiment.append(json_data[k])
        if k == 'probabilities':
            score.append(v[json_data['sentiment']])


data = [{'text':w, 'sentiment': s, 'score': t} for w, s, t in zip(text, sentiment, score)]

print(len(data))
print("\n\n\n")
print(data)

keys = data[0].keys()

with open('SA.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file,keys)
    writer.writeheader()
    writer.writerows(data)