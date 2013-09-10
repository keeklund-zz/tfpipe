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


class MachAdmix(Job):
    """New version of Markov Chain based haplotyper

    Not a module on Kure.  Needs to be built before use.

    """
    _cmd = 'mach-admix'
