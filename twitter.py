import os
import requests
import random
import urllib.request
import json
import twurl
import tweepy

TWITTER_URL = "https://api.twitter.com/1.1/friends/list.json"

def get_user_location(username):
    """Returns screen_name and location
    of user's friends"""

    url = twurl.augment(TWITTER_URL, {"screen_name": username, "count": 10})
    data = urllib.request.urlopen(url).read().decode()

    js = json.loads(data)
    # print(json.dumps(js))
    friends_data = []
    for u in js["users"]:
        user_location = (u["location"])
        user_screen_name = u["screen_name"]
        friends_data.append((user_location, user_screen_name))

    return friends_data
