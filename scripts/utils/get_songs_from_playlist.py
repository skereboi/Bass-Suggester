# Libraries
from ytmusicapi import YTMusic#, OAuthCredentials
import pandas as pd

# Load credentials
#ytm = YTMusic("../../.oauth.json", oauth_credentials=OAuthCredentials(client_id=client_id, client_secret=client_secret))
ytm = YTMusic("../../.browser.json")

# Get YTMusic playlist data
playlist_id = "PLP6srXm7y9EX8FIy4eOJ_GlxaehVgW9ms"
playlist_data = ytm.get_playlist(playlist_id, limit=1000)
playlist_title = playlist_data['title']
tracks = playlist_data['tracks']

# Parse songs data to dictionary

tracks_info = []

for track in tracks:

    # Extract multiple artist info
    artist_list = [artist['name'] for artist in track.get('artists', [])]
    # Parse list of artist to string
    artist_str = ", ".join(artist_list) if artist_list else None

    tracks_info.append({
        "title": track['title'],
        "artist": artist_str,
        "album": track['album']['name'] if track.get('album') else None ,
        "duration" : track.get('duration'),
        "videoId": track.get('videoId')
        })

#for song in tracks_info:
#    print(song)

df = pd.DataFrame(tracks_info)
print(df.head(10))
df.to_csv(f"{playlist_title}.csv", index=False)

#print(tracks)