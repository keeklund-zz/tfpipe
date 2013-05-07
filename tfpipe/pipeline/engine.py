"""Defines functionality for pipeline.

"""
from subprocess import Popen, PIPE, STDOUT
from tfpipe.utils import logger

class WorkFlow(object):
    """

    """
    def __init__(self, job_list=[], lsf=True):
        """Initialize WorkFlow.

        """
        self.jobs = job_list
        self.lsf = lsf
        logger.info("WorkFlow created")

    def _create_submit_str(self, job):
        """Build submission string.

        Use lsf scheduler, bsub, if self.lsf is True.

        """
        return (self._build_bsub(job) if self.lsf else '') + str(job)

    def _create_submit_list(self, job):
        """Build list of submission command.
        
        Use lsf scheduler, bsub, if self.lsf is True.

        """
        bsub = self._build_bsub(job).split() if self.lsf else []
        return bsub + job.show_as_list()
        
    def _dep_str(self, job):
        """Creates lsf dependency string.

        """
        return "&&".join([d.name for d in job.dep])

    def _build_bsub(self, job):
        """Create bsub command submission string.

        """
        bsub = "bsub -J %s -o ~/%s.out " % (job.name, job.name)
        bsub += "-w done(%s) " % self._dep_str(job) if job.dep else '' 
        return bsub

    def add_job(self, newjob):
        """ """
        pass

    def show(self):
        """Method shows all job submission strings and lists in WorkFlow.

        """
        for job in self.jobs:
            print self._create_submit_str(job)
#            print self._create_submit_list(job)
            logger.info("WorkFlow SHOW: %s" % 
                        self._create_submit_str(job))
            
    def run(self):
        """Method submits command string or list to shell.

        """
        for job in self.jobs:
            p = Popen(self._create_submit_list(job))
            retval = p.wait()
            logger.info("WorkFlow SUBMIT: %s" % 
                        self._create_submit_str(job))


# need ability to specify how dependency should work, whether 
# it's done, exited, ended, etc.


