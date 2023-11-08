
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# Authenticate with the Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

# Get the playlist ID of the playlist you want to shuffle
playlist_id = "YOUR_PLAYLIST_ID_HERE"

# Get the track IDs of all the tracks in the playlist
results = sp.playlist_tracks(playlist_id)
track_ids = [item["track"]["id"] for item in results["items"]]

# Shuffle the track IDs..
random.shuffle(track_ids)


# Replace the existing playlist with the shuffled list of track IDs
sp.playlist_replace_items(playlist_id, track_ids)
