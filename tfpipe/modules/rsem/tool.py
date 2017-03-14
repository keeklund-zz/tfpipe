""" """
from tfpipe.base import Job

class Rsemmod(Job):
    """

    """
    _module = 'rsem/1.2.31'

class Rsem_calculate_expression(Rsemmod):
    """

    """
    _cmd = 'rsem-calculate-expression'
    _memory_req_slurm = "200G"
    _memory_req_lsf = "48"
    _time_str_slurm = '"05:00:00"'