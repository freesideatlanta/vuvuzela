import logging
import sys

# shamlessly based off of: http://www.saltycrane.com/blog/2009/10/notes-python-logging

DEBUG_LOG_FILENAME = '/var/log/vuvuzela/debug.log'
SERVICE_LOG_FILENAME = '/var/log/vuvuzela/service.log'

# set up formatting
formatter = logging.Formatter('[%(asctime)s] %(levelno)s (%(process)d) %(module)s: %(message)s')

# set up logging to a file for all levels DEBUG and higher
debug_handler = logging.FileHandler(DEBUG_LOG_FILENAME)
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

# set up logging to a file for all levels WARNING and higher
service_handler = logging.FileHandler(SERVICE_LOG_FILENAME)
service_handler.setLevel(logging.WARN)
service_handler.setFormatter(formatter)

# create Logger object
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(debug_handler)
logger.addHandler(servie_handler)

# create shortcut functions
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
