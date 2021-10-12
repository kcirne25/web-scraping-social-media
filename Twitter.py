# Importing libraries
from typing import Dict
from pymongo import MongoClient
import tweepy as tw
import pandas as pd
import settings  # Contains keys, passwords and other settings

# Creating connection with MongoDB Atlas
client = MongoClient(settings.Mongo)

# Creating a Database with the name Data-Mining
mydb = client['Data-Mining']

# Creating Twtter's collection
collection = mydb['Twitter']

# OAuth Authentication
auth = tw.OAuthHandler(settings.Twitter_Consumer_Key, settings.Twitter_Consumer_Secret)
auth.set_access_token(settings.Twitter_Access_Token, settings.Twitter_Access_Secret)

# Creating twitter API
api = tw.API(auth, wait_on_rate_limit=True)

# Scraping data from Twitter
tweets_limit = 20 # Limit of tweets

# Creating empty lists to fetch data
ids = []
tweets = []
times = []
likes = []
sources = []
urls = []

# Adding data to lists
for i in tw.Cursor(api.user_timeline, id='kcirne25', tweet_mode='extended').items(tweets_limit):
    ids.append(i.id_str)
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    times.append(i.created_at)
    sources.append(i.source)
    urls.append(i.source_url)

# Creating a dictionary to store data 
dict = {'id':ids, 'tweet':tweets, 'time':times, 'likes':likes, 'source':sources, 'source_url':urls}
print(dict) # Printing to show in demo

df_tw = pd.DataFrame(data=dict)
df_tw.reset_index(inplace=True)
collection.insert_many(df_tw.to_dict('records')) 