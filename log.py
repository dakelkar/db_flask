import logging
from logging.handlers import RotatingFileHandler
import config


class Log(object):
    # This class wraps all logging operations.

    def __init__(self, log_path="", log_name=""):
        # Set up logging!
        log_formatter = logging.Formatter("%(levelname)s:%(name)s:%(asctime)s: %(message)s")
        if log_path == "" or log_name == "":
            log_file = config.LOG_PATH + config.LOG_NAME
        else:
            log_file = log_path + log_name

        my_handler = RotatingFileHandler(log_file, mode='a', maxBytes=512*1024, backupCount=2, encoding=None, delay=0)
        my_handler.setFormatter(log_formatter)
        my_handler.setLevel(logging.INFO)
        self.logger = logging.getLogger('root')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(my_handler)

    def get_logger(self):
        return self.logger
