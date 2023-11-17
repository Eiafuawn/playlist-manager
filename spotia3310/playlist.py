import os
import subprocess


class Playlist:
    def __init__(self, link, name, dir):
        self.link = link
        self.name = name
        self.dir = dir
        self.path = self.nameToPath()

    # Creates a path to the download target folder
    def nameToPath(self):
        dir_name = self.name.replace(" ", "-")
        # (location_folder + playlist_name w/o spaces)
        return os.path.join(self.dir, dir_name)

    def download(self):
        try:
            os.mkdir(self.path)
            print(f"Created {self.path} directory")
            # Launches the spotdl command using sync
            command = [
                "spotdl",
                "sync",
                self.link,
                "--save-file",
                "sync.spotdl"
            ]
            subprocess.run(command, check=True, cwd=self.path)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during download: {e}")


# class PlaylistExist(Exception):
#     def __init__(self, message, action, playlist):
#         super().__init__(message)
#         self.action = action
#         self.playlist = playlist

#     def perform_action(self):
#         choice = input(f"playlist: {self.playlist} exist already. Would you like to replace it? (yes or no)")
#         # todo
