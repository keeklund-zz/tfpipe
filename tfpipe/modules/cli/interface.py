""" """
from tfpipe.base import Job

class CLI(Job):
    _cmd = ''


class Gunzip(Job):
    """CLI for gunzip.

    """
    _cmd = '/bin/gunzip'


class Tar(Job):
    """

    """
    _cmd = '/bin/tar'


