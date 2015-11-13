""" """
from tfpipe.base import Job

class Bcl2FastqMod(Job):
    """

    """
    _module = 'bcl2fastq/1.8.4'


class Bcl2Fastq(Bcl2FastqMod):
    """

    """
    _cmd = 'bcl2fastq'


class ConfigureBcl2Fastq(Bcl2FastqMod):
    """

    """
    _cmd = 'configureBclToFastq.pl'


