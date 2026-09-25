import configparser


def read_config():
    config = configparser.ConfigParser()

    config.read("config/config.ini")

    return config["DEFAULT"]