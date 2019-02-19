from twitter_cursor_pagination import TwitterClient
import numpy as np
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt



class TweetAnalyzer():
    #structure tweet
    def tweets_to_data_frame(self,tweets):
        df=pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['tweets'])
        df['id']=np.array([tweet.id for tweet in tweets])
        df['len']=np.array([len(tweet.text) for tweet in tweets])
        df['date']=np.array([tweet.created_at for tweet in tweets])
        df['source']=np.array([tweet.source for tweet in tweets])
        df['likes']=np.array([tweet.favorite_count for tweet in tweets])
        df['retweets']=np.array([tweet.retweet_count for tweet in tweets])
        df['sentiment']=np.array([self.tweet_sentiment(tweet) for tweet in tweets])
        return df
    #text sentiment
    def sentiment(self,text):
        sentiment=TextBlob(text).sentiment.polarity
        return sentiment
    #tweet sentiment
    def tweet_sentiment(self,tweet):
        sentiment=TextBlob(tweet.text).sentiment.polarity
        if(sentiment==0):
            return 0
        elif(sentiment<0):
            return -1
        else:
            return 1

if __name__=="__main__":
    twitter_client=TwitterClient()
    tweet_analyzer=TweetAnalyzer()
    
    api=twitter_client.get_twitter_client_api()
    
    tweets=api.user_timeline(screen_name='realDonaldTrump',count=20)
    #print(dir(tweets[0]))
    df=tweet_analyzer.tweets_to_data_frame(tweets)
    #print(df.head(10))
    
    #get avg len over all tweets
    print(np.mean(df['len']))
    
    #get the number of likes overall tweets
    print(df)
    
    #Time Series
    time_likes=pd.Series(data=df['likes'].values,index=df['date'])
    time_likes.plot(figsize=(16,4),color='r')
    plt.show()

            
    
    

