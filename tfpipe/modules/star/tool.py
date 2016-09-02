""" """
from tfpipe.base import Job

class Starmod(Job):
    """

    """
    _module = 'star/2.5.1b'


class Star(Starmod):
    """

    """
    _cmd = 'star'
