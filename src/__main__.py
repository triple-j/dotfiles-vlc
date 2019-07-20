import logging

from argparse import ArgumentParser
from pathlib import Path

from pprint import pprint

from default_settings import DefaultSettings
from user_settings import UserSettings
from these_settings import TheseSettings

def main():
    #logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser(description="Configure VLC")

    args = parser.parse_args()

    logging.debug("Start Logging")

    default = DefaultSettings()
    user = UserSettings()
    these = TheseSettings(Path(__file__).parent / "assets")

    pprint(default.to_dict())
    pprint(user.to_dict())
    pprint(these.to_dict())

    combined = default.to_dict()
    combined.update(user.to_dict())
    combined.update(these.to_dict())

    pprint(combined)

    logging.info("Save combined configurations.")
    user.config.read_dict(combined)
    #user.write("/tmp/vlc-combined.conf", remove_empty_sections=True)
    user.write(remove_empty_sections=True)

if __name__ == "__main__":
    main()
