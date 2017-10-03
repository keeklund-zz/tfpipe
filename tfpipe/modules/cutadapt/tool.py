""" """
from tfpipe.base import Job

class Cutadaptmod(Job):
    """

    """
    _module = 'cutadapt'


class Cutadapt(Cutadaptmod):
    """

    """
    _cmd = 'cutadapt'
