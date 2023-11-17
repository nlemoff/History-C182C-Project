import spotipy
from spotipy.oauth2 import SpotifyOAuth

def current_track_info():
    # Set up the Spotify client
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                                   client_secret="YOUR_CLIENT_SECRET",
                                                   redirect_uri="YOUR_REDIRECT_URI",
                                                   scope="user-read-currently-playing"))

    # Fetch the current track
    current_track = sp.current_user_playing_track()
    if current_track is not None:
        title = current_track['item']['name']
        artist = current_track['item']['artists'][0]['name']
        return title, artist
    else:
        return "No song is currently playing."

if __name__ == "__main__":
    title, artist = current_track_info()
    print(f"Currently playing: {title} by {artist}")
