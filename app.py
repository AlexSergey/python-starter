import better_exceptions
from loguru import logger
from string import Template
import os

LOG = 'logs'

if not os.path.exists(LOG):
    os.makedirs(LOG)

better_exceptions.hook()

logger.start(Template("$logs/file_{time}.log").safe_substitute(logs=LOG))

logger.debug("That's it, beautiful and simple logging!")

