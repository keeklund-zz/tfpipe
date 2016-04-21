""" """
from tfpipe.base import Job

class FastQCMod(Job):
    """

    """
    _module = 'fastqc/0.11.3'

    
class Fastqc(FastQCMod):
    """Fastqc quality control.

    """
    _cmd = 'fastqc'

