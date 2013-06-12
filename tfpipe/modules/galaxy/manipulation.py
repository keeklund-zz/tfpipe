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
        # look for input and output, for cat/redirect
        jobs = [" ".join((self.cmd, 
                          self._parse_args(index, len(self.adapters)-1), 
                          '-a', 
                          adpt)) 
                for index, adpt in enumerate(self.adapters)]
        job_str = " | ".join(jobs)
        redirect = " %s %s " % (">", self.redirect) if self.redirect else ''
        return " ".join((job_str, redirect))

    def _parse_args(self, index=None, adpt_len=None):
        """Override base _parse_args to pipe jobs.

        """
        args = dict((str(k), str(v)) for k, v in self.args.iteritems())
        if index == 0:
            args.pop('-o', '--output')
        elif index == adpt_len:
            args.pop('-i', '--input')
        else:
            args.pop('-i', '--input')
            args.pop('-o', '--output')
        return " ".join([" ".join((str(k), str(v))) for k, v in args.iteritems()])
                         
    def add_adapter_file(self, apt_file):
        """Method allows user to submit multiple adapter sequences at once. 

        """
        with open(apt_file, 'r') as f:
            self.adapters = f.read().split()


class FastqQualityFilter(Galaxy):
    """Filters reads below specified quality.

    """
    _cmd = 'fastq_quality_filter'


class FastxTrimmer(Galaxy):
    """Trims reads to specified length.

    """
    _cmd = 'fastx_trimmer'


