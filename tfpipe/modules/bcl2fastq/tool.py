""" """
from tfpipe.base import job

class Bcl2Fastq2Mod(Job):
    """

    """
    _module = 'bcl2fastq2/2.17.1.4'


class Bcl2Fastq(Bcl2Fastq2Mod):
    """

    """
    _cmd = 'bcl2fastq'



