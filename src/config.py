import os
from configparser import RawConfigParser


# 取得設定檔的參數
def get_config() -> RawConfigParser:
    current_directory_path = os.path.dirname(__file__)
    config_file_path = os.path.join(current_directory_path, '../config.ini')
    config = RawConfigParser()
    config.read(config_file_path)

    return config
