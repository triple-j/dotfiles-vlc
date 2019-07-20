import logging

from pathlib import Path

from abstract_settings import Settings

class UserSettings(Settings):
    config_file_path = Path.home() / ".config/vlc/vlcrc"

    def __init__(self):
        # read config
        self.read()

