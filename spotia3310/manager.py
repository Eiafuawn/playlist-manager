import os
import shutil
from spotia3310.auth import user_library
from spotia3310.playlist import Playlist


def playlist_selection(path):
    results = user_library().current_user_playlists()
    playlists = results["items"]
    print("Select a playlist:")
    for idx, playlist in enumerate(playlists, 1):
        print(f"{idx}. {playlist['name']}")

    selection = input("Enter the number of the playlist you want to select: ")
    return Playlist(playlists[int(selection) - 1]["external_urls"]["spotify"],
                    playlists[int(selection) - 1]["name"], path)


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
