import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)


def user_library():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            redirect_uri="http://localhost:8888",
            scope="playlist-read-private",
        )
    )
    return sp
