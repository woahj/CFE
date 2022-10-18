import logging

#need to import os cause of this https://stackoverflow.com/a/64222858
import os
os.system("")

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38m"
    yellow = "\x1b[33m"
    red = "\x1b[31m"
    bold_red = "\x1b[31;1m"
    green = "\x1b[32m"
    reset = "\x1b[0m"
    format = "%(levelname)s: %(asctime)s - %(message)s"

    FORMATS = {
        logging.DEBUG: format + reset,
        logging.INFO: format + reset, 
        logging.WARNING: format + reset,
        logging.ERROR: format + reset,
        logging.CRITICAL: format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt,"%Y/%m/%d %H:%M:%S")
        return formatter.format(record)
