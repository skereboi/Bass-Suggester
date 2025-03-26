from ytmusicapi import YTMusic#, OAuthCredentials

# Load credentials
#ytm = YTMusic("../../.oauth.json", oauth_credentials=OAuthCredentials(client_id=client_id, client_secret=client_secret))
ytm = YTMusic("../../.browser.json")

# Get YTMusic playlists
library_playlists = ytm.get_library_playlists(limit=99) 
for playlist in library_playlists:
    print(f"Playlist: {playlist['title']} - ID: {playlist['playlistId']}")
