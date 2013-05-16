""" """
from tfpipe.base import Job

class Galaxy(Job):
    """Fastx-Toolkit 

    Fastq/a short-read pre-processing tools.

    http://hannonlab.cshl.edu/fastx_toolkit/index.html

    """
    _module = 'galaxy/1.0'


class FastqToFasta(Galaxy):
    """Use FastqToFasta to convert fastq to fasta file.

    """
    _cmd = 'fastq_to_fasta'
    # will need to add methods as necessary


class FastxClipper(Galaxy):
    """Use FastxClipper to remove or clip reads. 

    """
    _cmd = 'fastx_clipper'


class FastqQualityFilter(Galaxy):
    """Filters reads below specified quality.

    """
    _cmd = 'fastq_quality_filter'


