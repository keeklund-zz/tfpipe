"""Define exceptions to be used in tfpipe.

"""
from tfpipe.utils import logger

class InvalidInput(Exception):
    """Raise this exception when class receives irrelevant input.

    """
    def __init__(self, message):
        """Record the message passed.

        """
        self.message = message
        logger.warn(message)

    def __str__(self):
        return repr(self.message)


