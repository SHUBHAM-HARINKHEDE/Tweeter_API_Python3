from tweepy.streaming import StreamListener 
from tweepy import Stream
from twitter_credentials import auth
from tweet_analyzer import TweetAnalyzer
import json
from unidecode import unidecode
import sqlite3
conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE IF NOT EXISTS TWEETS
         (timestamp REAL PRIMARY KEY     NOT NULL,
         tweet           TEXT    NOT NULL,
         sentiment       REAL NOT NULL);''')
conn.execute('''CREATE INDEX IF NOT EXISTS  fast_timestamp ON TWEETS(timestamp)''')
conn.execute('''CREATE INDEX IF NOT EXISTS fast_tweet ON TWEETS(tweet)''')
conn.execute('''CREATE INDEX IF NOT EXISTS fast_sentiment ON TWEETS(sentiment)''')
conn.commit()

#inherit StreamListener of tweepy.straming
class StdOutListener(StreamListener):
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename=fetched_tweets_filename
        
    def on_data(self,data):
        try:
            print(data)
            with open(self.fetched_tweets_filename,'a') as tf:
                tf.write(data)
            data=json.loads(data)
            time_ms=data['timestamp_ms']
            tweet= unidecode(data['text'])
            sentiment_value=TweetAnalyzer().sentiment(tweet)
            with open('live_tweet.txt','a') as tf:
                tf.write(str(time_ms)+"$#%#"+str(sentiment_value)+"\n")
            
            conn.execute('''INSERT INTO TWEETS VALUES (?,?,?)''',(time_ms,tweet,sentiment_value))
    
            
            
        except BaseException as e:
            print("Error:%s"%str(e))
        return True
    
    def on_error(self,status):
        print(status)
#tweet streamer calls StdOutListener
class TwitterStreamer():
    def stream_tweets(self, fetched_tweets_filename,hash_tag_list):
        listener=StdOutListener(fetched_tweets_filename)
        stream=Stream(auth,listener)
        stream.filter(track=hash_tag_list)
        
if __name__=="__main__":
    hash_tag_list=['donald trump','narendra modi','surgical strick']
    fetched_tweets_filename="teets.json"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list)
    
    
            
    
    
   