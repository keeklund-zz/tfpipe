""" """
from tfpipe.base import Job

class Fseq(Job):
    """

    """
    _module = 'fseq/1.84'
    _cmd = 'fseq'

    # We are defaulting the memory here to 48 megs.
    # This command is killdevil LSF ONLY!
    _memory_req_lsf = "48"

class FseqJava(Job):
    """

    """
    _cmd = 'java -Xmx8000M -cp /proj/fureylab/code_repository/paulcotn/fseq/commons-cli-1.1.jar:/proj/fureylab/code_repository/paulcotn/fseq/fseq.jar edu.duke.igsp.gkde.Main '

    # This commmand is SLURM only
    _memory_req_slurm = "100G"