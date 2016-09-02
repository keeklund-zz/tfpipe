""" """
from tfpipe.base import Job

class Cutadaptmod(Job):
    """

    """
    _module = 'cutadapt/1.10'


class Cutadapt(Cutadaptmod):
    """

    """
    _cmd = 'cutadapt'
