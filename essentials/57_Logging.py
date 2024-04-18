import logging
from logging import DEBUG

# show the exception details by using the keyword argument exc_info=True

logging.critical("Critical Message")
logging.error   ("Error Message")
logging.warning ("Warning Message")
logging.info    ("Info Message")
logging.debug   ("Debug Message")

# or the general form
logging_level = DEBUG
logging.log(logging_level, "An exception was thrown!")
