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


class InvalidObjectCall(Exception):
    """Raise exception when object accessed illegally.

    """
    def __init__(self, message):
        """Log message.

        """
        self.message = message
        logger.warn(message)

    def __str__(self):
        return repr(self.message)


class DuplicateJobNames(Exception):
    """Raise exception when job names are not unique.

    """
    def __init__(self, message):
        """Log message.

        """
        self.message = message
        logger.warn(message)

    def __str__(self):
        return repr(self.message)


