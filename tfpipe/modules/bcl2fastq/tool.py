""" """
from tfpipe.base import Job

<<<<<<< HEAD
class Bcl2FastqMod(Job):
    """

    """
    _module = 'bcl2fastq/1.8.4'


class Bcl2Fastq(Bcl2FastqMod):
=======
class Bcl2Fastq2Mod(Job):
    """

    """
    _module = 'bcl2fastq2/2.17.1.4'


class Bcl2Fastq(Bcl2Fastq2Mod):
>>>>>>> 5849fd0f1c340591241e9b355e9175017f5b6407
    """

    """
    _cmd = 'bcl2fastq'


<<<<<<< HEAD
class ConfigureBcl2Fastq(Bcl2FastqMod):
    """

    """
    _cmd = 'configureBclToFastq.pl'


=======
>>>>>>> 5849fd0f1c340591241e9b355e9175017f5b6407
