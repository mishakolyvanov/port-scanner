import logging.config
from config.settings import LOG_SETTINGS
from .settings import *

logging.config.dictConfig(LOG_SETTINGS)

