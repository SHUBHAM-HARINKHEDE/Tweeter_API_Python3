from tweepy import Cursor
from twitter_credentials import auth,api 
import re     
class TwitterClient():
    def __init__(self,twitter_user=None):
        self.auth=auth
        self.twitter_client=api
        self.twitter_user=twitter_user
    def get_twitter_client_api(self):
        return self.twitter_client
    #user time line tweets
    def get_user_timelime_tweets(self,num_tweets):
        tweets=[]
        for tweet in Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    #friend list of 
    def get_friend_list(self,num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends,id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
    #home time line tweets of user
    def get_home_timeline_tweets(self,num_tweets):
        home_timeline_tweets=[]
        for tweet in Cursor(self.twitter_client.home_timeline,id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
            
if __name__=="__main__":  
    # for user name @narendramodi
    twitter_client=TwitterClient('narendramodi')
    #fetch tweets from user time line if use name not passed then by default it takes from your time line
    #print(twitter_client.get_user_timelime_tweets(2))
    #featching name of friends
    #print(twitter_client.get_friend_list(3))
    x = re.findall("'name':\s'[a-zA-Z0-9\s]*'", str(twitter_client.get_friend_list(2)))
    x=set(x)
    print(x)
    
    
    
    
   

