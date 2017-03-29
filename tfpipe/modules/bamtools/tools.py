""" """
from tfpipe.base import Job

class BamTools(Job):
    """

    """
    _module = 'bamtools/1.0.2'


class BamFilter(BamTools):
    """

    """
    _cmd = 'bamtools filter'
