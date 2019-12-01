import twitter
import pickle
import boto3
import json
import twitterConfig

def storeInDynamo(tweets):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TwitterCorpus')
    for tweet in tweets:
        table.put_item(
            Item = {
                'id': tweet.id_str,
                'user': tweet.user.screen_name,
                'text': tweet.full_text,
                'full_blob': json.dumps(tweet._json),
            }
        )


def addTimelineTweets():
    api = twitter.Api(consumer_key=twitterConfig.consumer_key,
                      consumer_secret=twitterConfig.consumer_secret,
                      access_token_key=twitterConfig.access_token_key,
                      access_token_secret=twitterConfig.access_token_secret,
                      tweet_mode='extended')


    timeline = api.GetHomeTimeline(count=200)
    print(len(timeline))
    tweets = timeline
    return tweets

def main():
    #uncomment to load new tweets
    tweets = addTimelineTweets()

    #store in dynamo
    #storeInDynamo(tweets)
    print(tweets)

def handler(event, lambda_context):
    main()

if __name__ == "__main__":
    main()

