import tweepy
import json


f = open('twitter-credentials.json')
credentials = json.load(f)

auth = tweepy.OAuthHandler(credentials['api_key'], credentials['api_secret_key'])
auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=credentials['bearer_token'])

user_fields = ['created_at', 'description', 'id', 'location', 'name',
               'pinned_tweet_id', 'profile_image_url', 'protected',
               'public_metrics', 'url', 'username', 'verified', 'withheld']

tweet_fields = ['attachments', 'author_id', 'conversation_id', 'created_at',
                'entities', 'id', 'in_reply_to_user_id', 'lang',
                'referenced_tweets', 'source', 'text', 'withheld']

user = client.get_user(username='POTUS', user_fields=user_fields)
user = {
        'id': user.data.id,
        'username': user.data.username,
        'name': user.data.name,
        'verified': user.data.verified,
        'created_at': user.data.created_at,
        'description': user.data.description,
        'profile_image_url': user.data.profile_image_url.replace('normal', '400x400'),
        'pinned_tweet_id': user.data.pinned_tweet_id,
        'protected': user.data.protected,
        'public_metrics': user.data.public_metrics,
        'entities': user.data.entities,
        'url': user.data.url,
        'withheld': user.data.withheld
    }

tweets = client.get_users_tweets(
    id=user['id'],
    max_results=1,
    tweet_fields=tweet_fields,
    exclude='retweets'
)

print(credentials)
print(user)
print(tweets)
