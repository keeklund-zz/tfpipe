""" """
from tfpipe.base import Job

class Fseq(Job):
    """

    """
    _module = 'fseq/1.84'
    _cmd = 'fseq'

    # We are defaulting the memory here to 48 megs.
    _memory_req_slurm = "100G"
    _memory_req_lsf = "48M"