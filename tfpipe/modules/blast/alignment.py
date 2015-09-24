""" """
from tfpipe.base import Job

class BlastMod(Job):
    """

    """
    _module = 'blast/2.2.31'


class BlastDBAliasTool(BlastMod):
    """

    """
    _cmd = 'blastdb_aliastool'

    
class BlastDBCheck(BlastMod):
    """

    """
    _cmd = 'blastdbcheck'


class BlastDBCMD(BlastMod):
    """

    """
    _cmd = 'blastdbcmd'

    
class BlastDBCp(BlastMod):
    """

    """
    _cmd = 'blastdbcp'

    
class BlastFormatter(BlastMod):
    """

    """
    _cmd = 'blast_formatter'


class BlastN(BlastMod):
    """

    """
    _cmd = 'blastn'

    
class BlastP(BlastMod):
    """

    """
    _cmd = 'blastp'


class BlastX(BlastMod):
    """

    """
    _cmd = 'blastx'


