import argparse
from spotia3310.manager import playlist_selection, modify_active_playlist


def main():
    args = parse_args()
    menu = int(input("What do you want to do?:\n" +
                     "1. Download a playlist\n" +
                     "2. Manage downloaded playlists\n"))
    if menu == 1:
        playlist = playlist_selection(args.dirpath)
        playlist.download()
    elif menu == 2:
        modify_active_playlist(args.dirpath)


def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "-d",
        "--dirpath",
        type=str,
        required=True,
        help="Target directory for downloads/management",
    )
    return ap.parse_args()
