import spotipy
import spotipy.util as util
import random

# Set up authentication with Spotify API
username = 'your_username'
scope = 'playlist-modify-public'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8888/callback'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Get the track IDs of all the tracks in the playlist
sp = spotipy.Spotify(auth=token)
playlist_id = 'your_playlist_id'
results = sp.playlist_tracks(playlist_id)
tracks = results['items']

# Sort the tracks based on the number of plays
tracks.sort(key=lambda x: x['track']['popularity'], reverse=True)

# Get the track IDs in the sorted order
track_ids = [track['track']['id'] for track in tracks]

# Create a new playlist to append the sorted playlist to
new_playlist_name = 'Sorted Playlist'
sp.user_playlist_create(username, new_playlist_name)

# Get the ID of the new playlist
playlists = sp.user_playlists(username)
new_playlist_id = None
for playlist in playlists['items']:
    if playlist['name'] == new_playlist_name:
        new_playlist_id = playlist['id']
        break

# Add the sorted tracks to the new playlist using the playlist_add_items() function
sp.playlist_add_items(new_playlist_id, track_ids)

# Print a success message
print('Playlist sorted and appended to new playlist successfully!')


