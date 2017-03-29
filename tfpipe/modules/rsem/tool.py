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