import logging
from configparser import ConfigParser

class Settings:
    config_file_path = None
    config = None

    def read(self):
        assert self.config_file_path is not None, "The path to the config file is not set"
        self.config = ConfigParser(strict=False)
        self.config.read(self.config_file_path, encoding="utf-8-sig")

    def to_dict(self):
        assert self.config is not None, "The config file has not been parsed"

        the_dict = {}

        for section in self.config.sections():
            section_dict = dict(self.config[section])

            if not section_dict:
                logging.debug(f"The '{section}' section is empty.  It will not be added.")
            else:
                the_dict[section] = section_dict

        return the_dict

    def write(self, file_path=None, remove_empty_sections=False):
        if file_path is None:
            file_path = self.config_file_path

        if remove_empty_sections:
            self.remove_empty_sections()

        with open(file_path, "w") as configfile:
            self.config.write(configfile, space_around_delimiters=False)

    def remove_empty_sections(self):
        assert self.config is not None, "The config file has not been parsed"

        for section in self.config.sections():
            section_dict = dict(self.config[section])

            if not section_dict:
                logging.debug(f"The '{section}' section is empty.  It will be removed.")
                self.config.remove_section(section)
