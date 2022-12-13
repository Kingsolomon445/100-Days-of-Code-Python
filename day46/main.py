from bs4 import BeautifulSoup
import requests
import spotipy
import os

# ---------------------------------AUTHORIZATION OF SPOTIPY------------------------------------------#
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

auth = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                   redirect_uri="http://example.com", scope="playlist-modify-private",
                                   show_dialog=False, requests_session=True, cache_path="token.txt")

access_token = auth.get_access_token(as_dict=False)

spotify = spotipy.client.Spotify(auth=access_token)
username = spotify.current_user()['display_name']
id = spotify.current_user()['id']

# -----------------------------------GETTING TOP 100 SONGS FROM BILL BOARD FOR CHOOSEN DATE---------------#
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
titles = soup.find_all('h3',
                       class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
top_100 = []
for title in titles:
    print(title.get_text().strip())
    top_100.append(title.get_text().strip())

# ---------------------------------GETTING URIS OF TOP 100 SONGS--------------------------------------------#
top_100_uris = []
year = date.split("-")[0]
for song in top_100:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        top_100_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlists = spotify.user_playlist_create(user=id, name=f"{date} Billboard 100.", public=False)
spotify.playlist_add_items(playlist_id=playlists["id"], items=top_100_uris)
