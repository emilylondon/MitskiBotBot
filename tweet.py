import tweepy
import secrets
from bot import get_song

auth = tweepy.OAuthHandler(secrets.api_key, secrets.api_key_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#get the original mitski bot as a user
mitski = api.get_user(screen_name='mitskilyricsbot')

#id of mitskilyricsbot user: 870648949983637505
print(mitski.id_str)
print(mitski.status.text)
tweet_id = mitski.status.id
lyrics = mitski.status.text
print(mitski.status.id_str)

#response string 
song, album = get_song(lyrics)
tweet = "@mitskilyricsbot The song is \"" + song + "\" from album " + album + "."
print(tweet)
api.update_status(status=tweet, in_reply_to_status_id = tweet_id)