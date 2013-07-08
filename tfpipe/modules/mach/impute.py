""" """
from tfpipe.base import Job

class Mach(Job):
    """Markov Chain based haplotyper

    Resolves long haplotypes or infer missing genotypes in samples of unrelated
    individuals.

    """
    _module = 'mach/1.0.18'


class Mach1(Mach):
    """

    """
    _cmd = 'mach1'

