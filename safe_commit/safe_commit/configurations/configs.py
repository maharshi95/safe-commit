# Author: Maharshi Gor
import configparser
import os
import os.path


class ConfigReader:
    def __init__(self):
        super(ConfigReader, self).__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_name = os.path.join(base_dir, "settings.ini")

        self.__config = configparser.ConfigParser(os.environ)
        self.__config.read(config_file_name)

    def get(self, section, key):
        return self.__config[section][key]

    def db_config(self, key):
        return self.get('DATABASE', key)
