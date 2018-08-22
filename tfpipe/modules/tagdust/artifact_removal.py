""" """
from tfpipe.base import Job

class TagDust(Job):
    """Eliminate artifacts from next generation sequencing data.

    http://www.ncbi.nlm.nih.gov/pubmed/19737799

    """
    _module = 'tagdust/1.13'
    _cmd = "tagdust"
