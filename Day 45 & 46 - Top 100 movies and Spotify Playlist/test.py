import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

YOUR_CLIENT_ID = "67da03ed1a72496698b9e5249fd6c424"
YOUR_CLIENT_SECRET="dbd24d6c44314e41b7ba5c94e6b3fefb"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=YOUR_CLIENT_ID,
                                                           client_secret=YOUR_CLIENT_SECRET))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])