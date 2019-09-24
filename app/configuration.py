from configparser import ConfigParser

FILE_CONFIG = r'printer.cfg'
options = {}


def load_config():
    """Parse config file"""
    config = ConfigParser()
    config.read_file(open(FILE_CONFIG))
    sections = config.sections()

    for s in sections:
        for opt in list(config.items(s)):
            key, value = opt
            try:
                options[key] = value
            except Exception as e:
                options[key] = False
