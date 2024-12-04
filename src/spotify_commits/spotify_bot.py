import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

def load_env():
    """Ensure .env file exists and load environment variables."""
    # Dynamically locate the .env file in the current working directory
    env_path = os.path.join(os.getcwd(), ".env")
    if not os.path.exists(env_path):
        raise FileNotFoundError("Missing .env file. Please run 'setup-spotify-env' to configure your API keys.")
    load_dotenv(dotenv_path=env_path)
    print("Environment Variables Loaded:")
    print(f"SPOTIPY_CLIENT_ID: {os.getenv('SPOTIPY_CLIENT_ID')}")
    print(f"SPOTIPY_CLIENT_SECRET: {os.getenv('SPOTIPY_CLIENT_SECRET')}")
    print(f"SPOTIPY_REDIRECT_URI: {os.getenv('SPOTIPY_REDIRECT_URI')}")
    

def get_current_song():
    """Fetch the currently playing song from Spotify."""
    load_env()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope="user-read-currently-playing user-read-playback-state"
    ))
    current_track = sp.current_playback()
    if current_track and current_track.get('is_playing'):
        song = current_track['item']['name']
        artist = ', '.join(artist['name'] for artist in current_track['item']['artists'])
        return f"{song} by {artist}"
    return "No song playing"

def main():
    try:
        print(get_current_song())
    except FileNotFoundError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
