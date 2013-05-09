"""Defines functionality for pipeline.

"""
from re import findall
from sys import exit
from subprocess import Popen, PIPE, STDOUT
from tfpipe.utils import logger

class WorkFlow(object):
    """WorkFlow creates and executes job submission statements.

    """
    def __init__(self, job_list=[], lsf=True):
        """Initialize WorkFlow.

        Method sets job lists and environment.  Depending on the environment, 
        job names are checked before submission.

        """
        self.jobs = job_list
        self.lsf = lsf
        self._check_jobnames()
        logger.info("WorkFlow created")

    def _check_jobnames(self):
        """Method to check job names for duplicates.

        WorkFlow terminates if duplicate is found in LSF mode.

        """
        job_names = [job.name for job in self.jobs]
        if (len(set(job_names)) == len(job_names)) and self.lsf:
            logger.info("WorkFlow job names are unique.")
        elif self.lsf:
            logger.warn("WorkFlow job names are NOT unique.")
            exit("WARNING: WorkFlow job names are NOT unique.")

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
        
    def _update_dep_str(self, job):
        """Updates lsf dependency string.

        """
        dep_options = findall(r"[\w']+", job.dep_str) 
        for depopt in set(dep_options):
            job.dep_str = job.dep_str.replace(depopt, depopt + "(%s)")
        job_deps = tuple([job.dep.get(jdo).pop(0).name for jdo in dep_options])
        return "-w %s " % (job.dep_str % job_deps)

    def _build_bsub(self, job):
        """Create bsub command submission string.

        """
        bsub = "bsub -J %s -o ~/%s.out " % (job.name, job.name)
        bsub += self._update_dep_str(job)
        return bsub

    def add_job(self, newjob):
        """ """
        pass

    def show(self):
        """Method shows all job submission strings and lists in WorkFlow.

        """
        for job in self.jobs:
            submit_str = self._create_submit_str(job)
            print submit_str
            logger.info("WorkFlow SHOW: %s" % submit_str)
            
    def run(self):
        """Method submits command list to shell.

        """
        for job in self.jobs:
            p = Popen(self._create_submit_list(job))
            retval = p.wait()
            logger.info("WorkFlow SUBMIT: %s" % 
                        self._create_submit_str(job))



