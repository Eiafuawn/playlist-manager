import os
import shutil
import subprocess

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

def spotify_user_library():
    # Set up authentication
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv(("CLIENT_SECRET")),
            redirect_uri="http://localhost:8888",
            scope="playlist-read-private",
        )
    )
    results = sp.current_user_playlists()
    return results["items"]


def playlist_selection(playlists):
    print("Select a playlist:")
    for idx, playlist in enumerate(playlists, 1):
        print(f"{idx}. {playlist['name']}")

    selection = input("Enter the number of the playlist you want to select: ")
    return [
        playlists[int(selection) - 1]["external_urls"]["spotify"],
        playlists[int(selection) - 1]["name"],
    ]


def display_menu(target_directory):
    menu = int(input("""What do you want to do?:\n
                     1. Download a playlist\n
                     2. Manage downloaded playlists"""))
    if menu == 1:
        playlists = spotify_user_library()
        selection = playlist_selection(playlists)
        playlist_handler(target_directory, selection)
    elif menu == 2:
        modify_active_playlist(target_directory)


def playlist_handler(target_directory, playlist):
    playlist_dir_name = playlist[1].replace(" ", "-")
    selected_playlist = os.path.join(target_directory, playlist_dir_name)
    if os.path.exists(target_directory):
        if os.path.exists(selected_playlist):
            print("Playlist already downloaded")
            modify_active_playlist(target_directory)
        else:
            os.makedirs(selected_playlist)
            print(f"Directory {selected_playlist} has been created")
            launch_spotdl(playlist[0], selected_playlist)
        print(f"Processing of files in {target_directory} complete")
    else:
        print(f"The directory {target_directory} does not exist on the drive.")


def modify_active_playlist(path):
    items = [
        item
        for item in os.listdir(path)
        if os.path.isdir(os.path.join(path, item)) or item.endswith(".zip")
    ]

    if not items:
        print(f"No directories or .zip files found in {path}")
        return

    print("Available directories and .zip files:")
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")

    choice = input(
        "Enter the number of the directory or .zip file you want to select: "
    )
    selected_item = items[int(choice) - 1]
    selected_item_path = os.path.join(path, selected_item)

    if os.path.isdir(selected_item_path):
        for item in items:
            if os.path.isdir(os.path.join(path, item)) \
              and item != selected_item:
                shutil.make_archive(
                    os.path.join(path, item), "zip", os.path.join(path, item)
                )
                shutil.rmtree(os.path.join(path, item))
                print(f"{os.path.join(path, item)} has been archived")

    elif selected_item_path.endswith(".zip"):
        shutil.unpack_archive(
            selected_item_path,
            os.path.join(path, selected_item.split(".zip")[0])
        )
        os.remove(selected_item_path)
        print(f"{selected_item} has been unarchived.")
        for item in items:
            if os.path.isdir(os.path.join(path, item)) \
              and item != selected_item:
                shutil.make_archive(
                    os.path.join(path, item), "zip", os.path.join(path, item)
                )
                shutil.rmtree(os.path.join(path, item))
                print(f"{os.path.join(path, item)} has been archived")
    else:
        print(
            f"Invalid selection: {selected_item} must be a dir or a zip file."
        )


def launch_spotdl(link, selected_playlist):
    try:
        os.chdir(selected_playlist)
        subprocess.run(["python", "-m", "spotdl", link], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    music_dir = r"D:\Music"
    display_menu(music_dir)
