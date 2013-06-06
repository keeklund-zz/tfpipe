""" """
from tfpipe.base import Job

class SamTools(Job):
    """

    """
    _module = 'samtools/0.1.19'


class View(SamTools):
    """

    """
    _cmd = 'samtools view '


class Sort(SamTools):
    """
    
    """
    _cmd = 'samtools sort '



