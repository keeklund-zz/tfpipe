"""Defines functionality for pipeline.

"""
from tfpipe.utils import logger

class WorkFlow(object):
    """

    """
    def __init__(self, job_list=[], lsf=True):
        self.jobs = job_list
        self.lsf = lsf
        logger.info("WorkFlow created")

    def _create_submit_str(self, job):
        return (self._build_bsub(job) if self.lsf else '') + str(job)

    def _create_submit_list(self, job):
        bsub = self._build_bsub(job).split() if self.lsf else []
        return bsub + job.show_as_list()
        
    def _dep_str(self, job):
        return "&&".join([d.name for d in job.dep])

    def _build_bsub(self, job):
        bsub = "bsub -J %s -o ~/%s.out " % (job.name, job.name)
        bsub += "-w done(%s) " % self._dep_str(job) if job.dep else '' 
        return bsub

    def add_job(self, newjob):
        """ """
        pass

    def show(self):
        for job in self.jobs:
            print self._create_submit_str(job)
            print self._create_submit_list(job)

    def run(self):
        pass


# need ability to specify how dependency should work, whether 
# it's done, exited, ended, etc.

