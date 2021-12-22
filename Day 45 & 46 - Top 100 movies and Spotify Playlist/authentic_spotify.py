import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import requests

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="67da03ed1a72496698b9e5249fd6c424",
                                               client_secret="dbd24d6c44314e41b7ba5c94e6b3fefb",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope=["user-read-private","playlist-modify-private"],
                                               show_dialog=True,
                                               cache_path="token.txt"))

username = sp.current_user()["id"]
print(username)
# playlists = sp.user_playlists('spotify')
# print(playlists)

# wrong, got response 403, insufficient client scope
# create_playlist_link = f"https://api.spotify.com/v1/users/{username}/playlists"
# header = {
#     "Authorization": "Bearer BQD2r3gWSjd4M9X14A8JPSDB6H7DHkP5_IVLPKm1AnYRL934X9LPYY5g7PCpzQ2COKrwmEWoStzS0zujBrepglEFJ6TQIbVLT3YREm98XXuOHFkdcJsQGEZOXcYncI__6DMp9ZTJwJB8y2grJaq90yE-jc8WjvmrDCzVs2QlxiA"
# }
#
# create_playlist = {
#     "name" : "Top 100 Billboard Songs",
#     "description" : "Trial Python courses"
#
# }
#
# response = requests.post(url = create_playlist_link, headers = header, json = create_playlist)
# print(response.text)

# works
# create_playlist = sp.user_playlist_create(user="1284430511", name="Top 100 Billboard", public=False, collaborative=False, description='Trial Python')
# print(create_playlist)

# not work
sp.playlist_add_items(playlist_id= "5yjEl5WWF1pkElLvDXxVM8", items="spotify:track:1rYYJVlUV2EcgehVUnwJvy")

# not work, get 401 error, no token provided
# song = "Firework"
# result = sp.search(q=f"track:{song}", type="track")
# print(result)

# not work, get illegal request
# search_track_link = f"https://api.spotify.com/v1/search"
# header = {
#     "Authorization": "Bearer BQD7FYlLkxbAR3vEi8JgNUa5d4qS1cijmFwa3Ret7rxfh2PueW_uj-WuQvluPeys2OnYmvbeVX8XM-7d4dO3L9GniKZAOjNFwRROB5Rsh9scTcaZwlrsRdGcnJ_8w6GomocIuf0ZIadCZ4ZDkgYJB0B6Xq9k9SH_OndlxJxZIXU"
# }
#
# search_track = {
#     "q" : "Alejandro",
#     "type" : "track"
# }
#
# response = requests.get(url = search_track_link, headers = header, json = search_track)
# print(response.text)