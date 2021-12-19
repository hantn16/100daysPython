from bs4 import BeautifulSoup
import pyperclip

import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
SPOTIFY_CLIENTID = "dfba6fcfeab846d780df1b5a859e4def"
SPOTIFY_SECRETKEY = "1daf1073ff744f3abb42893b756b396f"
SPOTIFY_APP_URI = "http://example.com"


def main():
    date = input(
        "Enter the date you want to search for top 100 songs (yyyy-MM-dd):")
    year = date.split("-")[0]
    res = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
    soup = BeautifulSoup(res.text, 'html.parser')
    song_tags = soup.select('li>ul>li>h3.c-title')
    songs = [x.getText().strip() for x in song_tags]

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENTID,
                                                   client_secret=SPOTIFY_SECRETKEY,
                                                   redirect_uri=SPOTIFY_APP_URI,
                                                   scope="playlist-modify-private",
                                                   show_dialog=True,
                                                   cache_path="musical_time_machine/token.txt"))
    song_uris = []

    for song in songs:
        results = sp.search(
            q=f'track: {song} year: {year}', limit=1, type='track')
        try:
            song_uris.append(results['tracks']['items'][0]['uri'])
        except IndexError:
            print(f"{song} not found in spotify")

    # results = sp.current_user_saved_tracks()
    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(idx, track['artists'][0]['name'], " – ", track['name'])


if __name__ == '__main__':
    main()
