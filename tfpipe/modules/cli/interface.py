""" """
from tfpipe.base import Job

class CLI(Job):
    _cmd = ''


class Gunzip(Job):
    """CLI for gunzip.

    """
    _cmd = '/bin/gunzip'


class Tar(Job):
<<<<<<< HEAD
    """CLI for tar.
=======
    """
>>>>>>> 5849fd0f1c340591241e9b355e9175017f5b6407

    """
    _cmd = '/bin/tar'


