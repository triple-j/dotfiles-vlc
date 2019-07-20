import logging

from configparser import ConfigParser
from os import unlink
from subprocess import run
from tempfile import NamedTemporaryFile

from pprint import pprint

from abstract_settings import Settings

class DefaultSettings(Settings):

    def __init__(self):
        # create temp config
        config_file = NamedTemporaryFile(prefix="vlc-default-", suffix=".conf", delete=False, mode="wt")
        self.config_file_path = config_file.name
        config_file.close()
        logging.debug(f"Create temporary config file: {self.config_file_path}")

        # populate config
        run([
            "vlc",
            "--intf", "dummy",
            "--config", self.config_file_path,
            "--reset-config",
            "vlc://quit",
        ], check=True)

        # read config
        self.read()

        # clean up
        unlink(self.config_file_path)
