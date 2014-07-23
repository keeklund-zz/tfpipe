""" """
from tfpipe.base import Job

class Qiime(Job):
    """

    """
    _module = 'qiime/1.8.0'


class JoinPairedEnds(Qiime):
    """

    """
    _cmd = 'join_paired_ends.py'


class ConvertFastaQualFastq(Qiime):
    """

    """
    _cmd = 'convert_fastaqual_fastq.py'
