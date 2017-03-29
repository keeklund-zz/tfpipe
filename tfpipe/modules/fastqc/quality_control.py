""" """
from tfpipe.base import Job

class FastQCMod(Job):
    """Now has own module not in galaxy.

    """
    _module = 'fastqc/0.11.3'
    _module_slurm = 'fastqc'

    
class Fastqc(FastQCMod):
    """Fastqc quality control.

    """
    _cmd = 'fastqc'

