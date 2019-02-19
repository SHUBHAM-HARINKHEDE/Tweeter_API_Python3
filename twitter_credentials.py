from tweepy import OAuthHandler
from tweepy import API
#API Authentication
consumer_key='PlaceYourConsumerKey' 
consumer_secret='PlaceYourConsumerSecret'

access_token='PlaceYourAccessToken'
access_token_secret='PlaceYourAccessTokenSecret'

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=API(auth)
