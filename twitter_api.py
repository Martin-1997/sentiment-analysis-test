import tweepy
import configparser


# read configparser
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')

api_key = config['twitter']['API_KEY']
api_key_secret = config['twitter']['API_KEY_SECRET']
bearer_token = config['twitter']['BEARER_TOKEN']
access_token = config['twitter']['ACCESS_TOKEN']
access_token_secret = config['twitter']['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()

# print(public_tweets)

client = tweepy.Client(bearer_token=bearer_token, access_token=access_token, access_token_secret=access_token_secret)

print(client.get_user(username='Martin_Zeitler1'))    
