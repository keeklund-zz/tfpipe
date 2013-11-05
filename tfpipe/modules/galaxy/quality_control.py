""" """
from tfpipe.base import Job
from manipulation import Galaxy

class Fastqc(Galaxy):
    """Galaxy's quality control.

    """
    _cmd = 'fastqc'
