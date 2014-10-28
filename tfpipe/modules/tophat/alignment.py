""" """
from tfpipe.base import Job

class TopHatMod(Job):
    """

    """
    _module = 'tophat/2.0.13'



class TopHat(TopHatMod):
    """

    """
    _cmd = 'tophat'



class TopHat2(TopHatMod):
    """

    """
    _cmd = "tophat2"


class TopHatFusionPost(TopHatMod):
    """

    """
    _cmd = 'tophat-fusion-post'  


class TopHatReports(TopHatMod):
    """

    """
    _cmd = 'tophat_reports'
