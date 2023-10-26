// First, you need to obtain an access token from Spotify
// You can find more information on how to do this here: https://developer.spotify.com/documentation/general/guides/authorization-guide/

// Then, you can use the access token to create a playlist
fetch('https://api.spotify.com/v1/users/{user_id}/playlists', {
    method: 'POST',
    headers: {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: 'My Playlist',
        description: 'A playlist created with the Spotify Web API',
        public: false
    })
})
.then(response => response.json())
.then(data => {
    const playlist_id = data.id;

    // Now that you have the playlist ID, you can add tracks to it
    fetch(`https://api.spotify.com/v1/playlists/${playlist_id}/tracks`, {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            uris: ['spotify:track:4iV5W9uYEdYUVa79Axb7Rh', 'spotify:track:1301WleyT98MSxVHPZCA6M']
        })
    })
    .then(response => response.json())
    .then(data => {
        // The tracks have been added to the playlist
        // You can now reorder and shuffle the tracks using the API
        // Here is an example of how to reorder the tracks
        fetch(`https://api.spotify.com/v1/playlists/${playlist_id}/tracks`, {
            method: 'PUT',
            headers: {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                range_start: 0,
                insert_before: 3,
                range_length: 1
            })
        })
        .then(response => response.json())
        .then(data => {
            // The tracks have been reordered
            // Here is an example of how to shuffle the tracks
            fetch(`https://api.spotify.com/v1/playlists/${playlist_id}/tracks`, {
                method: 'PUT',
                headers: {
                    'Authorization': 'Bearer ' + access_token,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    range_start: 0,
                    range_length: 2,
                    insert_before: 1,
                    shuffle: true
                })
            })
            .then(response => response.json())
            .then(data => {
                // The tracks have been shuffled
            });
        });
    });
});

const myArray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

const myData = myArray[2][1];

const myList = [
    ["Chocolate Bar", 15],
    ["Milk", 2],
    ["Bread", 1],
    ["Eggs", 12],
    ["Bananas", 6]
];
