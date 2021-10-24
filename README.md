# Web Scraping: Social Medias

Project developed to scrape data from social medias Twitter and Reddit.

## About the code

The code to fetch data was developed in Python, using the libraries Tweepy and Praw to connect with Twitter's and Reddit's APIs. The main purpose of the code is to connect with my personal users scrape tweets on Twitter and posts on Reddit and then store all the data in a MongoDB database in json format. To connect with MongoDB, the library pymongo was used.

## Data Models

### Twitter

Tweets were fetched from my user and the following information of the data model below was stored in MongoDB:
| Name | Description |
| ----------- | ----------- |
| Id | ID of the tweet |
| Tweet | Text of the tweet |
| Time | When the tweet was posted |
| Likes | How many likes does a tweet has |
| Source | Source of the data |
| Source_url | URL of the collected data |

### Reddit

Posts were fetched from my user and the following information of the data model below was stored in MongoDB:
| Name | Description |
| ----------- | ----------- |
| Id | ID of the tweet |
| Title | Title of the post |
| URL | URL of the post |
| Num_comment | Number of comments in the post |
| Score | Snumber of upvotes |
| Self_text | Text of the submitted post |

## User Interface

An User Interface developed with the library Flask was used to connect with my personal user in Twitter and Reddit. New tweets and posts can be created and inserted directly into my personal account using a Post request from Flask. The data is also stored in the MongoDB database. 

It can also be observed that the main goal of the project is the functionality of it, so the layout of the webpage was not the main objective.

## Conclusion

Twitter and Reddit found to be a powerful source of data and can provide up-to-date information. Python has a variety of tools to aid in this task and connect with other databases to store the results, like MongoDB.
