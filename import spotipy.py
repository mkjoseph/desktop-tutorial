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
results = sp.playlist_tracks(playlist_id)
tracks = results['items']
track_ids = [track['track']['id'] for track in tracks]

# Shuffle the track IDs using the random.shuffle() function
random.shuffle(track_ids)

# Create a new playlist to append the shuffled playlist to
new_playlist_name = 'Shuffled Playlist'
sp.user_playlist_create(username, new_playlist_name)

# Get the ID of the new playlist
playlists = sp.user_playlists(username)
new_playlist_id = None
for playlist in playlists['items']:
    if playlist['name'] == new_playlist_name:
        new_playlist_id = playlist['id']
        break

# Add the shuffled tracks to the new playlist using the playlist_add_items() function
sp.playlist_add_items(new_playlist_id, track_ids)

# Print a success message
print('Playlist shuffled and appended to new playlist successfully!')
