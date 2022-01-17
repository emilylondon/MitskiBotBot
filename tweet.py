import tweepy
import secret_info
from bot import get_song

auth = tweepy.OAuthHandler(secret_info.api_key, secret_info.api_key_secret)
auth.set_access_token(secret_info.access_token, secret_info.access_token_secret)

api = tweepy.API(auth)


def mitski_reply():
    #get the original mitski bot as a user
    mitski = api.get_user(screen_name='mitskilyricsbot')

    #id of mitskilyricsbot user: 870648949983637505
    #print(mitski.id_str)
    #print(mitski.status.text)
    tweet_id = mitski.status.id
    lyrics = mitski.status.text
    #print(mitski.status.id_str)

    #response string 
    song, album = get_song(lyrics)
    tweet = "@mitskilyricsbot \"" + song + "\" from album " + album + "."
    api.update_status(status=tweet, in_reply_to_status_id = tweet_id)

