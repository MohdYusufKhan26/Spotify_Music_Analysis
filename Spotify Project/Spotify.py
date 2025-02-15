import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# STEP 1: Set up your Spotify API credentials
SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))

# STEP 2: Load your dataset (assuming CSV format)
df = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')  

# STEP 3: Define a function to fetch album cover URL
def get_album_cover(track_name, artist_name):
    """Search for a track on Spotify and return the album cover image URL."""
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q=query, type="track", limit=1)
    
    if results["tracks"]["items"]:
        return results["tracks"]["items"][0]["album"]["images"][0]["url"]  
    return None  

# STEP 4: Apply the function to your dataset
df["cover_url"] = df.apply(lambda row: get_album_cover(row["track_name"], row["artist(s)_name"]), axis=1)

# STEP 5: Save the updated dataset
df.to_csv("spotify_tracks_with_covers.csv", index=False)
print("Updated dataset saved as 'spotify_tracks_with_covers.csv'")
