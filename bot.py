import tweepy
import secret_info
import requests



#Find song from lyrics
def get_song(lyrics):
    #Convert lyrics to list and remove words that include the ' character 
    phrase = lyrics.split(" ")
    apo = ['\'', '\n']
    new_phrase = [ele for ele in phrase if all(ch not in ele for ch in apo)]
    
    #Convert list back into string
    str = " "
    for ele in new_phrase:
        str += ele
        str += " "
        
    #Parameters for musixmatch API GET request to search lyrics to song 
    params = {
        'apikey': secret_info.mapi_key,
        'q_artist' : 'mitski',
        'q_lyrics' : str,
        's_track_rating' : 'desc',
    }

    response = requests.get('https://api.musixmatch.com/ws/1.1/track.search?', params)
    
    #Get song and album from response
    if response.status_code == 200: # Status: OK
        data = response.json()
        song = data['message']['body']['track_list'][0]['track']['track_name']
        album = data['message']['body']['track_list'][0]['track']['album_name']

    return song, album

song, album = get_song('')




