""" """
from tfpipe.base import Job

class SamTools(Job):
    """

    """
    _module = 'samtools/1.3'


class View(SamTools):
    """

    """
    _cmd = 'samtools view '


class Sort(SamTools):
    """
    
    """
    _cmd = 'samtools sort '
    _memory_req_slurm = "100G"


class Index(SamTools):
    """
    
    """
    _cmd = 'samtools index '


class FixMate(SamTools):
    """

    """
    _cmd = 'samtools fixmate'


