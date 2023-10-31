import spotipy
import spotipy.util as util
import os
import sys
import subprocess
import json
import requests
import random

# Authenticate with the Spotify API. You'll need to register your own application at https://developer.spotify.com/my-applications
username = 'your_username'
scope = 'playlist-modify-public'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8888/callback'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Create a new playlist in the user's Spotify account
if token:
    sp = spotipy.Spotify(auth=token)
    playlist_name = 'iTunes Playlist'
    playlist_description = 'Playlist imported from iTunes'
    sp.user_playlist_create(username, playlist_name, public=True, description=playlist_description)
    playlists = sp.user_playlists(username)
    playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
            break

    # Get the tracks from the user's iTunes library
    itunes_library_path = 'C:/Users/your_username/Music/iTunes/iTunes Music Library.xml'
    if not os.path.exists(itunes_library_path):
        print('iTunes library not found')
        sys.exit(1)
    itunes_library_xml = subprocess.check_output(['plutil', '-convert', 'json', '-o', '-', itunes_library_path])
    itunes_library = json.loads(itunes_library_xml)

    # Search for each track on Spotify using the Spotipy library
    track_uris = []
    for track in itunes_library['Tracks'].values():
        if 'Location' not in track:
            continue
        location = track['Location']
        if not location.startswith('file:///'):
            continue
        filepath = location[7:].replace('/', '\\')
        if not os.path.exists(filepath):
            continue
        title = track['Name']
        artist = track['Artist']
        query = f'track:{title} artist:{artist}'
        results = sp.search(q=query, type='track')
        if len(results['tracks']['items']) == 0:
            continue
        track_uri = results['tracks']['items'][0]['uri']
        track_uris.append(track_uri)

    # Shuffle the list of track URIs
    random.shuffle(track_uris)

    # Add each track to the new playlist in the user's Spotify account
    sp.user_playlist_add_tracks(username, playlist_id, track_uris)
else:
    print('Authentication failed')

# Path: desktop-tutorial/import%20spotipy.py
# then shuffle the playlist


