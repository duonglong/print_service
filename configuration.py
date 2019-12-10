from configparser import ConfigParser
from logging.config import fileConfig
import logging
import os

_logger = logging.getLogger("PRINT-SERVICE")

path = os.path.dirname(os.path.realpath(__file__))
LOGGING_CONFIG = path + '\\config\\logging.cfg'
FILE_CONFIG = path + '\\config\\printer.cfg'
GHOSTSCRIPT_PATH = path + "\\tools\\GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = path + "\\tools\\GSPRINT\\gsprint.exe"
PDF_PATH = path + "\\pdf\\"
LOG_PATH = path + "\\logs\\"
CHROMIUM_PATH = path + "\\local-chromium\\chrome_puppet.exe"

options = {}


def load_config():
    """Parse config file"""
    fileConfig(LOGGING_CONFIG)
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
    _logger.info("Default Printer: %s" % options.get("default_printer", ""))
