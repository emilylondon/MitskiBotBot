import tweepy
import secrets
import requests


# Authenticate to Twitter and Musixmatch
auth = tweepy.OAuthHandler(secrets.api_key, 
    secrets.api_key_secret)
auth.set_access_token(secrets.access_token, 
    secrets.access_token_secret)
print(secrets.api_key, secrets.api_key_secret)

api = tweepy.API(auth)

#Find song from lyrics
def get_song(lyrics):
    #convert lyrics to list and remove words that include the ' character 
    phrase = lyrics.split(" ")
    apo = ['\'']
    new_phrase = [ele for ele in phrase if all(ch not in ele for ch in apo)]
    
    #convert list back into string
    str = " "
    for ele in new_phrase:
        str += ele
        str += " "
        
    #parameters for musixmatch API GET request to search lyrics to song 
    params = {
        'apikey': secrets.mapi_key,
        'q_artist' : 'mitski',
        'q_lyrics' : str,
        's_track_rating' : 'desc',
    }

    response = requests.get('https://api.musixmatch.com/ws/1.1/track.search?', params)
    if response.status_code == 200: # Status: OK
        data = response.json()

    return data

data=get_song('I should tell them that I\'m not afraid to die')
#print(json.dumps(data, sort_keys=True, indent=4))
song = data['message']['body']['track_list'][0]['track']['track_name']
album = data['message']['body']['track_list'][0]['track']['album_name']
print("The song is \"" + song + "\" from " + album)


#api.update_status("Hello Tweepy")

#api = tweepy.API(auth, wait_on_rate_limit=True,
   # wait_on_rate_limit_notify=True)

