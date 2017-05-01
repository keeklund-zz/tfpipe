""" """
from tfpipe.base import Job

class Gsnap(Job):

    """Genomic Short-read Nucleotide Alignment Program.

    http://research-pub.gene.com/gmap/

    Add methods to this module as needed.

    """
    _module_slurm = 'gmap/2014-12-17'
    _cmd = "gsnap"
    #We are defaulting the memory here to 48 megs.
    _memory_req_slurm = "200G"
    _memory_req_lsf = "48"
    _time_str_slurm = '"05:00:00"'