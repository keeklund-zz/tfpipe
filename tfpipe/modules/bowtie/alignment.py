""" """
from tfpipe.base import Job

class BowTieMod(Job):
    """

    """
    _module = 'bowtie/1.1.0'


class BowTie(BowTieMod):
    """

    """
    _cmd = 'bowtie'


class BowTieAlignL(BowTieMod):
    """

    """
    _cmd = 'bowtie-align-l'


class BowTieAlignS(BowTieMod):
    """

    """
    _cmd = 'bowtie-align-s'


class BowTieBuild(BowTieMod):
    """

    """
    _cmd = 'bowtie-build'


class BowTieBuildL(BowTieMod):
    """

    """
    _cmd = 'bowtie-build-l'


class BowTieBuildS(BowTieMod):
    """

    """
    _cmd = 'bowtie-build-s'


class BowTieInspect(BowTieMod):
    """

    """
    _cmd = 'bowtie-inspect'


class BowTieInspectL(BowTieMod):
    """

    """
    _cmd = 'bowtie-inspect-l'


class BowTieInspectS(BowTieMod):
    """

    """
    _cmd = 'bowtie-inspect-s'
