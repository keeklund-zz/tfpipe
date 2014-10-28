""" """
from tfpipe.base import Job

class SRAToolkit(Job):
    """

    """
    _module = 'sratoolkit/2.3.2-4'


class BamLoad(SRAToolkit):
    """

    """
    _cmd = 'bam-load'


class BamLoad2(SRAToolkit):
    """

    """
    _cmd = 'bam-load.2'



class BamLoad232(SRAToolkit):
    """

    """
    _cmd = 'bam-load.2.3.2'


class FastQDump(SRAToolkit):
    """

    """
    _cmd = 'fastq-dump'


class FastQDump2(SRAToolkit):
    """

    """
    _cmd = 'fastq-dump.2'      


class FastQDump232(SRAToolkit):
    """

    """
    _cmd = 'fastq-dump.2.3.2'


class FastQLoad(SRAToolkit):
    """

    """
    _cmd = 'fastq-load'        


class FastQLoad2(SRAToolkit):
    """

    """
    _cmd = 'fastq-load.2'      


class FastQLoad232(SRAToolkit):
    """

    """
    _cmd = 'fastq-load.2.3.2'
