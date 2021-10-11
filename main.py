# Importing libraries
from flask import Flask
from flask import request, render_template
from praw.models.listing.mixins import subreddit
from pymongo import MongoClient
import tweepy as tw
import praw  # Python Reddit API Wrapper
import settings  # Contains keys, secrets and other settings

# OAuth Authentication
auth = tw.OAuthHandler(settings.Twitter_Consumer_Key, settings.Twitter_Consumer_Secret)
auth.set_access_token(settings.Twitter_Access_Token, settings.Twitter_Access_Secret)

# Creating web app with Flask
app = Flask(__name__)  # Flask constructor

@app.route('/')
def home():
    return render_template('index.html')  # Main page

# Twitter
@app.route('/PostTweet', methods=['POST', 'GET'])
def PostTweets():
    api = tw.API(auth, wait_on_rate_limit=True)

    # Creating connection with MongoDB Atlas
    client = MongoClient(settings.Mongo)
    db = client['Data-Mining']
    collection = db['Twitter']

    # Code to create post request on Twitter
    if request.method == 'POST':
        TweetForm = str(request.form['NewTweet'])
        post = api.update_status(TweetForm)
        collection.insert_one({'id': post.id_str,
                               'tweet': post.text,
                               'time': post.created_at,
                               'likes': post.favorite_count,
                               'source': post.source,
                               'source_url': post.source_url,
                               })
        result = True
    else:
        result = False
    return render_template('PostTweet.html', res=result)
    
# Reddit
@app.route('/PostReddit', methods=['POST', 'GET'])
def PostReddit():
    reddit = praw.Reddit(client_id = settings.Reddit_Client_Id, client_secret = settings.Reddit_Client_Secret,
                         user_agent = settings.Reddit_User_Agent, username = settings.Reddit_Username,
                         password = settings.Reddit_Password)

    # Creating connection with MongoDB Atlas
    client = MongoClient(settings.Mongo)
    db = client['Data-Mining']
    collection = db['Reddit']

    # Code to create post request on Reddit
    if request.method == 'POST':
        TitleReddit = str(request.form['titlePost'])
        FormReddit = str(request.form['NewReddit'])
        subReddit = reddit.subreddit("u_" + settings.Reddit_Username)
        newReddit = subReddit.submit(TitleReddit, FormReddit)

        collection.insert_one({'title': newReddit.title,
                               'id': newReddit.id,
                               'url': newReddit.num_comments,
                               'num_comment': newReddit.num_comments,
                               'score': newReddit.score,
                               'self_text': newReddit.selftext,
                               })
        result = True
    else:
        result = False
    return render_template('PostReddit.html', res = result)

# Running flask
if __name__ == "__main__":
    app.run(debug=True)
