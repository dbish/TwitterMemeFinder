#!/usr/bin/env python
# coding: utf-8

# In[13]:

# get tweets from corpus
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TwitterCorpus')
response = table.scan()
data = response['Items']

# In[25]:
# page through until the end of all data
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

# In[34]:
# setup plotting inline
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# function to cleanup tweets
# note: twitter doesn't count things like @mentions and certain links towards the char count
def normalizeTweet(tweet):
    # lowercase
    tweet = tweet.lower()

    # split up
    tweet = tweet.split()

    # take out @mentions and links/images for purposes of tweet length
    newTweet = []
    for word in tweet:
        if (word[0] != '@') and ('http' not in word):
            if word == '&amp;':
                word = '&'
            newTweet.append(word)

    # merge back
    tweet = ' '.join(newTweet)

    return tweet


# In[105]:


# get text normalized
tweets_normalized = [normalizeTweet(x['text']) for x in data]

# In[107]:

# take out retweets for this analysis
no_rt_tweets = []
for tweet in tweets_normalized:
    try:
        if tweet.split()[0] != 'rt':
            no_rt_tweets.append(tweet)
    except:
        pass

# In[110]:
# get lengths of tweets
tweetLengths = [len(x) for x in no_rt_tweets]

# In[120]:
# plot lengths
plt.hist(tweetLengths, 20)



