import spotipy
from spotipy import SpotifyOAuth, SpotifyClientCredentials
from ytmusicapi import YTMusic
import Config
from pprint import pprint
def get_spotify_playlist():

    scope = 'user-library-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Config.Client_ID, redirect_uri= Config.Redirect_URI, client_secret= Config.Client_Secret, scope=scope))
    os = 0
    rlimit = 50
    total = int(sp.current_user_saved_tracks()["total"] /rlimit)
    songnames = []
    test = 34
    for x in range(total):

        results = sp.current_user_saved_tracks(offset=os, limit=rlimit)
        for idx, item in enumerate(results['items']):
            track = item['track']
            try:
                print(track['artists'][0]['name'], " - ", track['name'])
                songnames.append(str(track['name'] + " " + track['artists'][0]['name']))
            except:
                print("invalid char")

        os += 50

    finalids = []
    yt = YTMusic('headers_auth.json')

    for song in songnames:
        try:
            id = yt.search(query=song, filter='songs')[0].get('videoId')
            finalids.append(id)
            print(id)

        except:
            print("something happened..")

    yt.create_playlist(title="spotify", description="auto generated from spotify playlist", video_ids=finalids)
    f.close()

get_spotify_playlist()
