# Author: Maharshi Gor
import configparser
import os
import os.path as osp

from safe_commit.configurations import configs


class ConfigReader:
    def __init__(self):
        super(ConfigReader, self).__init__()
        base_dir = os.path.dirname(osp.abspath(__file__))
        config_file_name = osp.join(base_dir, "settings.ini")

        self.__config = configparser.ConfigParser(os.environ)
        self.__config.read(config_file_name)

        user_home_dir = osp.expanduser('~')
        self.__base_dir_path = osp.join(user_home_dir, configs.BASE_DIR_NAME)

    def get(self, section, key):
        return self.__config[section][key]

    def db_config(self, key):
        return self.get('DATABASE', key)

    def git_config(self, key):
        return self.get('GIT', key)
    
    @property
    def base_dir_path(self):
        return self.__base_dir_path
