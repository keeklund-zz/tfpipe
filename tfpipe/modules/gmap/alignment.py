""" """
from tfpipe.base import Job

class Gsnap(Job):

    """Genomic Short-read Nucleotide Alignment Program.

    http://research-pub.gene.com/gmap/

    Add methods to this module as needed.

    """
    _module_slurm = 'gmap/2014-12-17'
    _cmd = "gsnap"
