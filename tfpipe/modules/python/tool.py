""" """
from tfpipe.base import Job

class Pythonmod(Job):
    """

    """
    _module = 'python/2.7.6'
    _module_slurm = 'python/2.7.12'

class Python(Pythonmod):
    """

    """
    _cmd = 'python'
