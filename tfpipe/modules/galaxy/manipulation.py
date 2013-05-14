""" """
from tfpipe.base import Job

class Galaxy(Job):
    _module = 'galaxy'


class FastqToFasta(Galaxy):
    """Use FastqToFasta to convert fastq to fasta file.

    Examples:
    ---------
    >>> from tfpipe.modules.galaxy import FastqToFasta
    >>> fq2a = FastqToFasta()
    >>>
    >>> fq2a = FastqToFasta(cmd='override_binary')

    """

    _cmd = 'fastq_to_fasta'
    # will need to add methods as necessary


class FastxClipper(Galaxy):
    """Use FastxClipper to remove or clip reads. 

    """

    _cmd = 'fastx_clipper'


class FastqQualityFilter(Galaxy):
    """

    """
    _cmd = 'fastq_quality_filter'


