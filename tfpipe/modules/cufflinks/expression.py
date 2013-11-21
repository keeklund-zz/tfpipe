""" """
from tfpipe.base import Job

class CuffLinksModule(Job):
    """

    """
    _module = 'cufflinks/2.1.1'


class CuffCompare(CuffLinksModule):
    """

    """
    _cmd = 'cuffcompare'


class CuffDiff(CuffLinksModule):
    """

    """
    _cmd = 'cuffdiff'


class CuffLinks(CuffLinksModule):
    """

    """
    _cmd = 'cufflinks'


class CuffMerge(CuffLinksModule):
    """

    """
    _cmd = 'cuffmerge'
