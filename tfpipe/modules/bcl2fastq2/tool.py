""" """
from tfpipe.base import Job

class Bcl2Fastq2Mod(Job):
    """ 

    """
    _module = 'bcl2fastq2/2.18.0.12'


class Bcl2Fastq2(Bcl2Fastq2Mod):
    """

    """
    _cmd = 'bcl2fastq'
