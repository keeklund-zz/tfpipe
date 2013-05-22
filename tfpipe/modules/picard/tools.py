""" """
from tfpipe.base import Job

class Picard(Job):
    """

    """
    _module = 'picard/1.88'


class MarkDuplicates(Picard):
    """

    """
    _cmd = '/nas02/apps/picard-1.88/picard-tools-1.88/MarkDuplicates.jar'


