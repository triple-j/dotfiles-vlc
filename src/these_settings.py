import logging

from configparser import ConfigParser
from os import unlink
from pathlib import Path
from tempfile import NamedTemporaryFile

from abstract_settings import Settings

class TheseSettings(Settings):

    def __init__(self, config_path):
        config_files = list(Path(config_path).glob("**/*.conf"))

        # create temp config
        config_file = NamedTemporaryFile(prefix="vlc-these-", suffix=".conf", delete=False, mode="wt")
        self.config_file_path = config_file.name

        for a_config_path in config_files:
            rel_path = Path(a_config_path).relative_to(config_path)
            config_file.write("\n")
            config_file.write(f"##START FILE: {rel_path}")
            config_file.write("\n")

            with open(a_config_path, "r") as a_config_file:
                config_file.write(a_config_file.read())

            config_file.write("\n")
            config_file.write(f"##END FILE: {rel_path}")
            config_file.write("\n\n")

        config_file.close()

        # read config
        self.read()

        # clean up
        unlink(self.config_file_path)
