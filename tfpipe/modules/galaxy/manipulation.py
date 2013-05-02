""" """
from tfpipe.base import CommandLine

class FastqToFasta(CommandLine):
    """Use FastqToFasta to convert fastq to fasta file.

    Examples:
    ---------
    >>> from tfpipe.modules.galaxy import FastqToFasta
    >>> fq2a = FastqToFasta()
    >>>
    >>> fq2a = FastqToFasta(cmd='override_binary')

    """

    _cmd = 'fastq_to_fasta'

    # will need to add methods


class FastxClipper(CommandLine):
    """Use FastxClipper to remove or clip reads. 

    """

    _cmd = 'fastx_clipper'

