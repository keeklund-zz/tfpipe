""" """
from tfpipe.base import Job

class Rsemmod(Job):
    """

    """
    _module = 'rsem/1.2.23'


class Rsem(Rsemmod):
    """

    """
    _cmd = 'rsem'
