# Importing libraries
import praw  # Python Reddit API Wrapper
import pandas as pd
from pymongo import MongoClient


# Connecting with MongoDB Atlas
client = MongoClient("Your_MongoDB_Connection_String")

# Accessing Database with the name Data-Mining
db = client['Data-Mining']

# Creating Reddit's collection
collection = db['Reddit']

# OAuth Authentication
reddit = praw.Reddit(client_id = "Your_Reddit_Client_Id", client_secret = "Your_Reddit_Client_Secret",
                    user_agent = "Your_Reddit_User_Agent", username = "Your_Reddit_Username",
                    password = "Your_Reddit_Password")

# Using the class redditor to fetch data
PostReddit = []

for i in reddit.redditor("Your_Reddit_Username").submissions.top():
    PostReddit.append([i.title, i.id, i.url, i.num_comments, i.score, i.selftext])

print(PostReddit) # Printing to show in demo

# Creating dictionary to import to MongoDB
PostReddit = pd.DataFrame(PostReddit, columns=['title', 'id', 'url', 'num_comments', 'score', 'text'])
PostReddit.reset_index(inplace=True)
dic_reddit = PostReddit.to_dict('records')
collection.insert_many(dic_reddit)

