"""Defines functionality for pipeline.

"""
from tfpipe.utils import logger

class WorkFlow(object):
    """

    """
    def __init__(self, job_list=[]):
        self.jobs = job_list
        logger.info("WorkFlow created")

    def _create_submit_str(self, job):
        return self._build_bsub(job) + str(job)

    def _create_submit_list(self, job):
        bsub = self._build_bsub(job).split()
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

    # check order of jobs
    def show(self):
        for job in self.jobs:
            print self._create_submit_str(job)
            print self._create_submit_list(job)

# need ability to specify how dependency should work, whether 
# it's done, exited, ended, etc.

