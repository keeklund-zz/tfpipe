"""Defines functionality for pipeline.

"""
from tfpipe.utils import logger

class WorkFlow(object):
    """

    """
    def __init__(self, job_list=[]):
        self.jobs = job_list
        logger.info("WorkFlow created")

    def add_job(self, newjob):
        """ """
        pass

    # check order of jobs
    def show(self):
        for job in self.jobs:
            print self._create_submit_str(job)
    
    def _create_submit_str(self, job):
        bsub = "bsub -J %s " % job.name
        tmp = "&&".join([d.name for d in job.dep])
        bsub += "-w done(%s) " % tmp if job.dep else '' 
        return bsub + str(job)
# possible to add attributes to job from within workflow?
# need ability to specify how dependency should work, whether 
# it's done, exited, ended, etc.

