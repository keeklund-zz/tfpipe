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
    
    def __init__(self, **inputs):
        """

        """
        super(FastqToFasta, self).__init__(**inputs)
        if self.cmd is None:
            self.cmd = self._cmd

