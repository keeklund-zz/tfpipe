""" """
from tfpipe.base import Job

class Picard(Job):
    """

    """
    _module = 'picard/2.2.4'


class MarkDuplicates(Picard):
    """

    """
    _cmd = 'java -Xmx4g -jar /nas02/apps/picard-2.2.4/picard-tools-2.2.4/picard.jar MarkDuplicates'


class MergeSamFiles(Picard):
    """

    """
    _cmd = 'java -Xmx4g -jar /nas02/apps/picard-2.2.4/picard-tools-2.2.4/picard.jar MergeSamFiles'


class SortSamFiles(Picard):
    """

    """
    _cmd = 'java -Xmx4g -jar /nas02/apps/picard-2.2.4/picard-tools-2.2.4/picard.jar SortSam'
