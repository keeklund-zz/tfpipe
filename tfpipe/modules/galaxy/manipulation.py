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

    def __str__(self):
        """Represent object as string.

        Override base class to pipe multiple adapter sequences.

        """
        job_str = ''
        for adpt in self.adapters:
            tmp = " ".join((self.cmd, self._parse_args(), '-a', adpt))
            job_str = " | ".join((job_str, tmp))
        redirect = " %s %s " % (">", self.redirect) if self.redirect else ''
        return " ".join((job_str, redirect))

    def add_adapter_file(self, apt_file):
        """Method allows user to submit multiple adapter sequences at once. 

        """
        with open(apt_file, 'r') as f:
            self.adapters = f.read().split()


class FastqQualityFilter(Galaxy):
    """Filters reads below specified quality.

    """
    _cmd = 'fastq_quality_filter'


